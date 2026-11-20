# Sistema Inteligente de Detección de Precios

Prototipo desarrollado en **Python** para la recolección, análisis y comparación de precios de productos de la canasta básica en supermercados colombianos, con el propósito de identificar posibles anomalías mediante técnicas de análisis estadístico.

El sistema realiza consultas automatizadas en los supermercados **Éxito y Carulla**, procesa la información recolectada y presenta los resultados a través de un dashboard interactivo.

## Tecnologías utilizadas

- **Python 3.11:** lenguaje principal de desarrollo.
- **Selenium:** automatización del navegador y extracción de información mediante web scraping.
- **Pandas:** procesamiento y manipulación de datos.
- **Matplotlib:** generación de gráficos estadísticos.
- **Plotly:** visualización interactiva de datos.
- **Streamlit:** desarrollo del dashboard interactivo.
- **Git y GitHub:** control de versiones y gestión del repositorio.

## Funcionalidades

- Recolección automatizada de productos y precios.
- Normalización y procesamiento de la información.
- Análisis estadístico de los precios.
- Identificación de posibles anomalías.
- Comparación de precios entre supermercados.
- Generación de rankings y gráficos.
- Dashboard para consultar los resultados y filtrar la información.
- Exportación de resultados en archivos CSV.

## Ejecución del proyecto

### 1. Requisitos previos

- Python 3.11.
- Google Chrome.
- ChromeDriver compatible con la versión instalada de Google Chrome.

### 2. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Y despues abrimos la carpeta ejecutando el siguiente comando.

```bash
cd Proto-Func-Detector-Precios
```

### 3. Crear y activar el entorno virtual

```bash
py -3.11 -m venv venv
```

Despues de crear el entorno virtual, ahora lo activamos en este caso en Windows es así:

```bash
venv\Scripts\activate
```

Mientras que tanto para MacOS y Linux es de la siguiente manera:

```bash
source venv/bin/activate
```

Y en caso de que se use otra shell en Unix (csh/fish) es de la siguiente forma:

```bash
source venv/bin/activate.csh
``` 
o 

```bash
source venv/bin/activate.fish
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar ChromeDriver

El módulo de scraping utiliza Selenium y busca el controlador mediante la ruta chromedriver.exe.

Se debe disponer de un ChromeDriver compatible con Google Chrome y colocarlo en la ubicación esperada por modulos/scraper.py, o ajustar la ruta en dicho archivo.

### 6. Ejecutar el sistema

Para ejecutarlo primero se necesita iniciar el proceso de recolección y análisis, para lo cual se ejecuta el siguiente comando:

```bash
python main.py
```

Y por ultimo para iniciar el dashboard interactivo, se ejecuta este comando:

```bash
streamlit run dashboard.py
```

El dashboard permite consultar los productos recolectados, comparar precios, visualizar posibles anomalías y explorar los resultados mediante gráficos y filtros.

## Estructura del proyecto

Esta es la estructura del proyecto:

```text
Proto-Func-Detector-Precios/
│
├── data/                  # Datos y resultados del análisis
│
├── modulos/               # Módulos de procesamiento y análisis
│   ├── analisis.py
│   ├── comparacion.py
│   ├── estadisticas.py
│   ├── graficos.py
│   ├── normalizacion.py
│   ├── ranking.py
│   └── scraper.py
│
├── dashboard.py           # Dashboard interactivo
├── main.py                # Ejecución principal del sistema
├── requirements.txt       # Dependencias del proyecto
├── .gitignore
└── README.md
```

## Consideraciones

- La extracción de información depende de la estructura y disponibilidad de los sitios web de los supermercados.
- Los resultados pueden variar según los precios y productos disponibles al momento de la consulta.
- Las anomalías identificadas son alertas estadísticas y no constituyen por sí mismas una prueba de precios abusivos.