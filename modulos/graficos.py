import matplotlib.pyplot as plt


def generar_grafico_ranking(ranking):

    supermercados = ranking.index

    precios = ranking.values

    plt.figure(figsize=(9, 5))

    barras = plt.bar(supermercados, precios, color=["royalblue", "seagreen"])

    plt.title(
        "Comparación de precios promedio por supermercado",
        fontsize=14,
        fontweight="bold",
    )

    plt.xlabel("Supermercado", fontsize=12)

    plt.ylabel("Precio promedio (COP)", fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # Mostrar valores encima de las barras
    for barra in barras:
        altura = barra.get_height()

        plt.text(
            barra.get_x() + barra.get_width() / 2,
            altura,
            f"${altura:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.tight_layout()

    plt.savefig("data/grafico_ranking.png", dpi=300)

    plt.close()
