def ranking_supermercados(df):

    ranking = df.groupby("Supermercado")["Precio_Num"].mean().sort_values()

    return ranking
