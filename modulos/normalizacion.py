import re


def limpiar_nombre(nombre):

    nombre = nombre.lower()

    nombre = re.sub(r"[^a-z0-9 ]", "", nombre)

    nombre = nombre.replace("gramos", "g")
    nombre = nombre.replace("gr", "g")

    nombre = nombre.strip()

    return nombre
