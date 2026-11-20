import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def obtener_exito(marca, paginas):

    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    productos = []

    urls = []

    for pagina in range(paginas):
        urls.append(
            f"https://www.exito.com/mercado?brand={marca}&category-2=despensa&facets=brand%2Ccategory-2&sort=score_desc&page={pagina}"
        )

    patrocinados_detectados = 0
    for url in urls:
        print(f"\nEntrando a: {url}")

        driver.get(url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
        )

        items = driver.find_elements(By.CSS_SELECTOR, "article")

        for item in items:
            texto = item.text

            lineas = [linea.strip() for linea in texto.split("\n") if linea.strip()]

            if len(lineas) < 2:
                continue

            nombre = lineas[0]

            # Segunda validación de seguridad
            if nombre.upper() == "PATROCINADO":
                patrocinados_detectados += 1

                print(f"⚠ Producto patrocinado detectado en {marca.upper()} - {url}")

                if len(lineas) > 1:
                    nombre = lineas[1]
                else:
                    continue

            precio = "0"

            for linea in lineas:
                if "$" in linea and "Gr a" not in linea:
                    precio = linea.strip()
                    break

            productos.append(
                {
                    "Marca": marca.upper(),
                    "Supermercado": "Exito",
                    "Producto": nombre,
                    "Precio_Texto": precio,
                }
            )

        if patrocinados_detectados > 0:
            print(f"✔ Productos patrocinados corregidos: {patrocinados_detectados}")

    driver.quit()

    return pd.DataFrame(productos)


def obtener_carulla(marca, paginas):

    service = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    productos = []

    urls = []

    for pagina in range(paginas):
        urls.append(
            f"https://www.carulla.com/despensa?brand={marca}&category-1=despensa&facets=brand%2Ccategory-1&sort=score_desc&page={pagina}"
        )

    patrocinados_detectados = 0
    for url in urls:
        print(f"\nEntrando a: {url}")

        driver.get(url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
        )

        items = driver.find_elements(By.CSS_SELECTOR, "article")

        for item in items:
            texto = item.text

            lineas = [linea.strip() for linea in texto.split("\n") if linea.strip()]

            if len(lineas) < 2:
                continue

            nombre = lineas[0]

            # Segunda validación de seguridad
            if nombre.upper() == "PATROCINADO":
                patrocinados_detectados += 1

                print(f"⚠ Producto patrocinado detectado en {marca.upper()} - {url}")

                if len(lineas) > 1:
                    nombre = lineas[1]
                else:
                    continue

            precio = "0"

            for linea in lineas:
                if "$" in linea and "Gr a" not in linea:
                    precio = linea.strip()
                    break

            productos.append(
                {
                    "Marca": marca.upper(),
                    "Supermercado": "Carulla",
                    "Producto": nombre,
                    "Precio_Texto": precio,
                }
            )

        if patrocinados_detectados > 0:
            print(f"✔ Productos patrocinados corregidos: {patrocinados_detectados}")

    driver.quit()

    return pd.DataFrame(productos)


"""def obtener_jumbo():

    service = Service("chromedriver.exe")

    driver = webdriver.Chrome(service=service)

    productos = []

    urls = [
        "https://www.jumbocolombia.com/supermercado/despensa/diana?initialMap=c,c&initialQuery=supermercado/despensa&layout=grid&map=category-1,category-2,brand"
    ]

    for url in urls:
        print(f"\nEntrando a: {url}")

        driver.get(url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
        )

        items = driver.find_elements(By.CSS_SELECTOR, "article")

        for item in items:
            texto = item.text
            print("\n--- PRODUCTO JUMBO ---")
            print(texto)

            if "DIANA" not in texto.upper():
                continue

            if "SUAVIZANTE" in texto.upper():
                continue

            lineas = texto.split("\n")

            if len(lineas) < 2:
                continue

            nombre = lineas[0]

            precio = "0"

            for linea in lineas:
                if "$" in linea and "Gr a" not in linea:
                    precio = linea.strip()

                    break

            productos.append(
                {"Supermercado": "Jumbo", "Producto": nombre, "Precio_Texto": precio}
            )

    driver.quit()

    return pd.DataFrame(productos)


def obtener_olimpica():

    service = Service("chromedriver.exe")

    driver = webdriver.Chrome(service=service)

    productos = []

    urls = [
        "https://www.olimpica.com/diana/despensa-app-19?initialMap=productClusterIds&initialQuery=17185&map=brand,productclusternames&page=2"
    ]

    for url in urls:
        print(f"\nEntrando a: {url}")

        driver.get(url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
        )

        items = driver.find_elements(By.CSS_SELECTOR, "article")

        for item in items:
            texto = item.text
            print("\n--- PRODUCTO JUMBO ---")
            print(texto)

            if "DIANA" not in texto.upper():
                continue

            if "SUAVIZANTE" in texto.upper():
                continue

            lineas = texto.split("\n")

            if len(lineas) < 2:
                continue

            nombre = lineas[0]

            precio = "0"

            for linea in lineas:
                if "$" in linea and "Gr a" not in linea:
                    precio = linea.strip()

                    break

            productos.append(
                {"Supermercado": "Olimpica", "Producto": nombre, "Precio_Texto": precio}
            )

    driver.quit()

    return pd.DataFrame(productos)


def obtener_makro():

    service = Service("chromedriver.exe")

    driver = webdriver.Chrome(service=service)

    productos = []

    urls = ["https://tienda.makro.com.co/ca/mercado-y-alimentos/CP_01?brands=DIANA"]

    for url in urls:
        print(f"\nEntrando a: {url}")

        driver.get(url)

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
            )

        except TimeoutException:
            print("No se encontraron productos en Makro.")

            driver.quit()

            return pd.DataFrame()

        items = driver.find_elements(By.CSS_SELECTOR, "article")

        for item in items:
            texto = item.text

            if "DIANA" not in texto.upper():
                continue

            if "SUAVIZANTE" in texto.upper():
                continue

            lineas = texto.split("\n")

            if len(lineas) < 2:
                continue

            nombre = lineas[0]

            precio = "0"

            for linea in lineas:
                if "$" in linea and "Gr a" not in linea:
                    precio = linea.strip()

                    break

            productos.append(
                {"Supermercado": "Makro", "Producto": nombre, "Precio_Texto": precio}
            )

    driver.quit()

    return pd.DataFrame(productos)"""
