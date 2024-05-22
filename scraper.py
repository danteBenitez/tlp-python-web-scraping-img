import requests
import url as urlutils
from bs4 import BeautifulSoup
from urllib import parse
from pathlib import Path

def read_html_from(url: str):
    """
        Lee HTML de forma remota y lo interpreta usando BeautifulSoup
    """
    try:
        response = requests.get(url)
        if not response.ok:
            raise FileNotFoundError(f"Archivo no encontrado en {url}")
        plain_response = response.text
        html = BeautifulSoup(plain_response, features="html.parser")
        return html
    except requests.exceptions.ConnectionError as err:
        print("Ha ocurrido un error de conexión: ", err)
    except Exception as err:
        print(err)

def download_image(dir: str, url: str):
    """
        Descarga la imagen en `url` en el directorio `dir`.
    """
    img = requests.get(url).content
    complete_path = dir + "/" + urlutils.get_filename_from_url(url)
    with open(complete_path, "b+w") as file:
        file.write(img)

ALLOWED_EXTENSIONS = ["jpg", "png", "webp"]

def scrap_images(absolute_url: str, folder: str, *, verbose: bool):
    """
        Descarga todas las imágenes referenciadas en el documento
        HTML en `url` en el directorio `folder`
    """
    html = read_html_from(absolute_url)
    images = html.find_all('img', attrs={
        'src': True
    })
    parsed = parse.urlparse(absolute_url)
    domain_and_scheme = parsed.scheme + "://" + parsed.netloc

    for image in images:
        url = image["src"]
        if url.startswith('//'):
            url = parsed.scheme + ':' + url
        if url.startswith('/'):
            url = domain_and_scheme + url
        elif url.startswith('.'):
            url = domain_and_scheme + url[:1]

        if verbose:
            print(f"Visitando {url}")
        extension = urlutils.get_extension_from_url(url)
        if extension in ALLOWED_EXTENSIONS:
            if verbose:
                print(f"Descargando {url}")
            download_image(folder, url)
