def comparar_precios(df):

    comparacion = df.pivot_table(
        index="Producto_Normalizado",
        columns="Supermercado",
        values="Precio_Num",
        aggfunc="mean",
    ).reset_index()

    comparacion = comparacion.dropna()

    if "Exito" in comparacion.columns and "Carulla" in comparacion.columns:
        comparacion["Diferencia"] = (
            comparacion["Carulla"] - comparacion["Exito"]
        ).abs()

    return comparacion
