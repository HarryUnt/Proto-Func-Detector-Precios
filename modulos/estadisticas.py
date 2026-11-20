def calcular_estadisticas(df):

    promedio = df["Precio_Num"].mean()

    mediana = df["Precio_Num"].median()

    maximo = df["Precio_Num"].max()

    minimo = df["Precio_Num"].min()

    desviacion = df["Precio_Num"].std()

    return {
        "Promedio": promedio,
        "Mediana": mediana,
        "Maximo": maximo,
        "Minimo": minimo,
        "Desviacion": desviacion,
    }
