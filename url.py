from urllib import parse
from pathlib import Path

def get_filename_from_url(url: str):
    """
        Obtiene el nombre de un archivo presente en una cierta URL.
    """
    file_path = parse.urlparse(url).path.split('/')[-1]
    return file_path

def get_extension_from_url(url: str):
    """
        Obtiene la extensión de un archivo presente en una cierta URL.
    """
    file_path = get_filename_from_url(url)
    return file_path.split('.')[-1]