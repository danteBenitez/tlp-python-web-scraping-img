from scraper import scrap_images
import sys
import os

def print_help():
    """
        Imprimir la ayuda del programa.
    """
    print("Uso: python3 __init__.py <url> [--folder <folder>]")
    print("Descargar todas las imágenes de la página web <url> en la carpeta <folder>.")
    print("Si no se especifica <folder>, se descargará en la carpeta ./imagenes.")
    sys.exit(0)

def ensure_exists(folder: str):
    """
        Comprobar si la carpeta <folder> existe, y si no, crearla.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

def main():
    """
        Inicializar el web scraper de la pagina web pasada por parámetros.
    """
    if len(sys.argv) >= 2 and sys.argv[1] == "help":
        print_help()

    folder = './imagenes'
    if "--folder" in sys.argv:
        folder = sys.argv[sys.argv.index("--folder") + 1]
        sys.argv.remove("--folder")
        sys.argv.remove(folder)

    verbose = False 
    if "--verbose" in sys.argv:
        sys.argv.remove("--verbose")
        verbose = True

    url = ""
    try:
        url = sys.argv[1]
    except:
        print("[ERROR] URL no especificada. ")
        print_help()

    # Remover un / sobrante
    if url.endswith('/'):
        url = url.removesuffix('/')

    ensure_exists(folder)

    scrap_images(url, folder, verbose=verbose)

if __name__ == "__main__":
    main()
