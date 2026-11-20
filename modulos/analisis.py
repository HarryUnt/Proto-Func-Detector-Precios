def detectar_anomalias(df):

    promedio = df["Precio_Num"].mean()

    desviacion = df["Precio_Num"].std()

    limite_superior = promedio + (2 * desviacion)

    limite_inferior = promedio - (2 * desviacion)

    df["Anomalia"] = (df["Precio_Num"] > limite_superior) | (
        df["Precio_Num"] < limite_inferior
    )

    return df
