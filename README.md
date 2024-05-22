# Práctica Web Scraping 2: Obtención de imágenes con Python

## Criterios
- Funcionalidad: El web scraper debe ser capaz de recorrer el sitio web de manera efectiva y extraer todas
las etiquetas &lt;img&gt; con sus atributos src.
Debe descargar cada imagen encontrada y guardarla en una carpeta especificada. La carpeta debe ser validada: si no existe, debe ser creada automáticamente. Solo se deben descargar imágenes con los formatos png, jpg y webp.
- Manejo de Errores:
El programa debe manejar adecuadamente situaciones de error, como im&aacute;genes no encontradas, errores de conexión, o problemas de formato de HTML.
Si una imagen no se puede descargar, el programa debe continuar con la siguiente.
- Legibilidad y Organización del Código: El código debe estar bien organizado y estructurado, con nombres descriptivos de
variables y funciones.
- Presentación del Trabajo Práctico: La presentación del trabajo práctico debe realizarse en un repositorio de GitHub, el cual debe ser público para su posterior revisión y evaluación.

### Objetivo:
- El objetivo de este trabajo práctico es implementar un web scraper en Python que pueda recorrer un sitio web, extraer todas las etiquetas &lt;img&gt; con sus atributos src y descargar cada imagen en una carpeta llamada "imagenes". Si la carpeta no existe, el programa debe crearla autom&aacute;ticamente. Solo se deben descargar im&aacute;genes con los formatos png, jpg y webp.

### Notas Adicionales:
- Se deben usar la librería BeautifulSoup y requests.
- El programa primero válida si la carpeta existe y, de no ser así, se debe crear.
- Se recorren todas las etiquetas &lt;img&gt; de la página dada, se obtienen los enlaces src y se descargan las imágenes en la carpeta especificada, siempre y cuando sean de los formatos png, jpg, y webp.
- Se manejan errores de conexión y descarga para asegurar que el programa no se detenga ante cualquier problema.

## Sobre el proyecto

### Requerimientos

- Python en su última versión
- `pip` y `venv`

### Pasos para inicializar el proyecto

- Crear y activar entorno virtual

```bash
$ python3 -m venv .env
$ source .env/bin/activate
# o
$ .env/Scripts/activate
```
- Instalar las dependencias:

```bash
$ pip install -r requirements.txt
```

- Ver opciones de uso del script principal: 

```bash
$ python3 __init__.py help
```

