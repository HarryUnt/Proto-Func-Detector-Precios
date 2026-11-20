import pandas as pd

from modulos.analisis import detectar_anomalias
from modulos.comparacion import comparar_precios
from modulos.estadisticas import calcular_estadisticas
from modulos.graficos import generar_grafico_ranking
from modulos.normalizacion import limpiar_nombre
from modulos.ranking import ranking_supermercados
from modulos.scraper import obtener_carulla, obtener_exito

# =====================================================
# CONFIGURACIÓN DE MARCAS
# =====================================================

marcas = {
    "diana": {"exito": 3, "carulla": 3},
    "doria": {"exito": 3, "carulla": 3},
    "el-rey": {"exito": 3, "carulla": 3},
    "san-jorge": {"exito": 5, "carulla": 4},
    "zenu": {"exito": 3, "carulla": 3},
    "corona": {"exito": 2, "carulla": 2},
}

print("=== SISTEMA DETECTOR DE PRECIOS ===")

# =====================================================
# RECOLECCIÓN DE DATOS
# =====================================================

print("\n[1/4] Recolectando datos desde supermercados...")

dfs = []

for marca, config in marcas.items():
    print(f"\nProcesando marca: {marca.upper()}")

    df_exito = obtener_exito(marca, config["exito"])

    print(f"✔ Éxito: {len(df_exito)} productos")

    df_carulla = obtener_carulla(marca, config["carulla"])

    print(f"✔ Carulla: {len(df_carulla)} productos")

    dfs.append(df_exito)
    dfs.append(df_carulla)

df = pd.concat(dfs, ignore_index=True)

print("\n=== PRODUCTOS POR MARCA ===")
print(df["Marca"].value_counts())

print("\n=== PRODUCTOS POR SUPERMERCADO ===")
print(df["Supermercado"].value_counts())

# =====================================================
# NORMALIZACIÓN
# =====================================================

print("\n[2/4] Normalizando productos...")

df["Producto_Normalizado"] = df["Producto"].apply(limpiar_nombre)

df["Precio_Num"] = (
    df["Precio_Texto"]
    .str.replace(".", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace(r"[^0-9]", "", regex=True)
    .astype(float)
)

print("✔ Normalización completada.")

# =====================================================
# ESTADÍSTICAS
# =====================================================

print("\n[3/4] Calculando estadísticas...")

estadisticas = calcular_estadisticas(df)

print("✔ Estadísticas generadas.")

print("\n=== RESULTADOS ===")

print(f"Promedio: ${estadisticas['Promedio']:,.0f}")
print(f"Mediana: ${estadisticas['Mediana']:,.0f}")
print(f"Máximo: ${estadisticas['Maximo']:,.0f}")
print(f"Mínimo: ${estadisticas['Minimo']:,.0f}")
print(f"Desviación estándar: ${estadisticas['Desviacion']:,.0f}")

# =====================================================
# DETECCIÓN DE ANOMALÍAS
# =====================================================

print("\n[4/4] Detectando anomalías...")

df = detectar_anomalias(df)

anomalias = df[df["Anomalia"]]

anomalias.to_csv(
    "data/anomalias_detectadas.csv", sep=";", index=False, encoding="utf-8-sig"
)

print("\n=== DETECCIÓN DE ANOMALÍAS ===")

if len(anomalias) > 0:
    print(anomalias[["Supermercado", "Producto", "Precio_Num"]].to_string(index=False))

else:
    print("No se detectaron anomalías.")

# =====================================================
# COMPARACIÓN ENTRE SUPERMERCADOS
# =====================================================

print("\n=== COMPARACIÓN ENTRE SUPERMERCADOS ===")

comparacion = comparar_precios(df)

print(comparacion.head(10).to_string(index=False))

print("\n✔ Comparación realizada.")

# =====================================================
# RANKING DE SUPERMERCADOS
# =====================================================

print("\n=== RANKING DE SUPERMERCADOS ===")

ranking = ranking_supermercados(df)

for supermercado, valor in ranking.items():
    print(f"{supermercado}: ${valor:,.0f}")

print(f"\n Supermercado más económico: {ranking.index[0]}")

generar_grafico_ranking(ranking)

print("\n✔ Visualización gráfica generada correctamente.")

# =====================================================
# EXPORTAR CSV
# =====================================================

df.to_csv("data/productos_marcas.csv", sep=";", index=False, encoding="utf-8-sig")

comparacion.to_csv(
    "data/comparacion_precios.csv", sep=";", index=False, encoding="utf-8-sig"
)

print("\n✔ Sistema ejecutado correctamente.")
print("✔ CSV de productos generado.")
print("✔ CSV de comparación generado.")
print("✔ CSV de anomalías generado.")
print("✔ Gráfico de ranking generado.")
