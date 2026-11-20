import pandas as pd
import plotly.express as px
import streamlit as st

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Sistema Inteligente de Detección de Precios",
    page_icon="📊",
    layout="wide",
)

st.badge("Versión Final - Proyecto de Tesis")

st.title("Sistema Inteligente de Detección de Precios")

st.caption("Comparación automática de precios entre supermercados colombianos")

st.markdown(
    """
    Visualización y análisis de precios de múltiples marcas
    mediante técnicas de scraping web, análisis estadístico
    y detección de anomalías.
    """
)

# =====================================================
# CARGAR DATOS
# =====================================================

df = pd.read_csv("data/productos_marcas.csv", sep=";")

comparacion = pd.read_csv("data/comparacion_precios.csv", sep=";")

anomalias = pd.read_csv("data/anomalias_detectadas.csv", sep=";")

# =====================================================
# PANEL LATERAL
# =====================================================

st.sidebar.title("Panel de Control")

st.sidebar.markdown("---")

st.sidebar.header("Filtros")

opciones_marcas = ["Todas"]
opciones_marcas.extend(sorted(df["Marca"].dropna().unique().tolist()))

marca = st.sidebar.radio(
    "Marca",
    ["Todas"] + sorted(df["Marca"].unique().tolist()),
)

opciones_supermercados = ["Todos"]
opciones_supermercados.extend(sorted(df["Supermercado"].dropna().unique().tolist()))

supermercado = st.sidebar.radio(
    "Supermercado",
    ["Todos"] + sorted(df["Supermercado"].unique().tolist()),
)

df_filtrado = df.copy()

if marca != "Todas":
    df_filtrado = df_filtrado[df_filtrado["Marca"] == marca]

if supermercado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Supermercado"] == supermercado]

st.sidebar.markdown("---")

st.sidebar.info(
    f"""
    Productos: {len(df_filtrado):,}

    Marcas: {df_filtrado["Marca"].nunique()}

    Supermercados: {df_filtrado["Supermercado"].nunique()}
    """
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Seleccione una marca o supermercado para actualizar automáticamente los resultados."
)

# =====================================================
# REINDEXAR DESDE 1
# =====================================================

df_filtrado = df_filtrado.reset_index(drop=True)
df_filtrado.index = df_filtrado.index + 1

# =====================================================
# MÉTRICAS
# =====================================================

st.header("Estadísticas Generales")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Productos", len(df_filtrado))

col2.metric("Marcas", df_filtrado["Marca"].nunique())

col3.metric("Promedio", f"${df_filtrado['Precio_Num'].mean():,.0f}")

col4.metric("Anomalías", int(df_filtrado["Anomalia"].sum()))

st.success(f"Se cargaron correctamente {len(df_filtrado)} registros.")

# =====================================================
# GRÁFICO PROMEDIOS
# =====================================================

st.header("Promedio de precios por supermercado")

if supermercado == "Todos":
    promedios = df_filtrado.groupby("Supermercado")["Precio_Num"].mean().reset_index()

    fig = px.bar(
        promedios,
        x="Supermercado",
        y="Precio_Num",
        color="Supermercado",
        text_auto=".0f",
        title="Promedio de precios por supermercado",
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Seleccione 'Todos' los supermercados para visualizar la comparación.")

# =====================================================
# DISTRIBUCIÓN POR MARCA
# =====================================================

st.header("Productos por marca")

# El gráfico ignora el filtro de marca,
# pero sí respeta el filtro de supermercado

if supermercado == "Todos":
    datos_pie = df
else:
    datos_pie = df[df["Supermercado"] == supermercado]

productos_marca = datos_pie["Marca"].value_counts().reset_index()

productos_marca.columns = ["Marca", "Cantidad"]

fig_marcas = px.pie(
    productos_marca,
    names="Marca",
    values="Cantidad",
    title="Distribución de productos por marca",
)

st.plotly_chart(fig_marcas, use_container_width=True)

# =====================================================
# PESTAÑAS
# =====================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Productos",
        "Comparación",
        "Anomalías",
        "Ranking",
    ]
)

# =====================================================
# PRODUCTOS
# =====================================================

with tab1:
    st.subheader("Productos recolectados")

    tabla_productos = df_filtrado.reset_index()

    tabla_productos = tabla_productos.rename(columns={"index": "ID"})

    tabla_productos = tabla_productos.drop(
        columns=["Producto_Normalizado"], errors="ignore"
    )

    st.data_editor(
        tabla_productos,
        use_container_width=True,
        disabled=True,
        hide_index=True,
        column_config={
            "ID": st.column_config.NumberColumn(
                "ID",
                width="small",
            ),
            "Marca": st.column_config.TextColumn(
                "Marca",
                width="small",
            ),
            "Supermercado": st.column_config.TextColumn(
                "Supermercado",
                width="small",
            ),
            "Producto": st.column_config.TextColumn(
                "Producto",
                width="large",
            ),
            "Precio_Texto": st.column_config.TextColumn(
                "Precio",
                width="small",
            ),
            "Precio_Num": st.column_config.NumberColumn(
                "Precio Numérico",
                width="small",
            ),
            "Anomalia": st.column_config.CheckboxColumn(
                "Anomalía",
                width="small",
            ),
        },
    )

# =====================================================
# COMPARACIÓN
# =====================================================

with tab2:
    st.subheader("Comparación entre supermercados")

    comparacion_tabla = comparacion.reset_index()

    comparacion_tabla = comparacion_tabla.rename(columns={"index": "ID"})

    comparacion_tabla["ID"] += 1

    st.data_editor(
        comparacion_tabla, use_container_width=True, disabled=True, hide_index=True
    )

# =====================================================
# ANOMALÍAS
# =====================================================

with tab3:
    st.subheader("Anomalías detectadas")

    if len(anomalias) > 0:
        anomalias_tabla = anomalias.reset_index()

        anomalias_tabla = anomalias_tabla.rename(columns={"index": "ID"})

        anomalias_tabla["ID"] += 1

        st.data_editor(
            anomalias_tabla, use_container_width=True, disabled=True, hide_index=True
        )

    else:
        st.success("No se detectaron anomalías.")

# =====================================================
# RANKING
# =====================================================

with tab4:
    st.subheader("Ranking de supermercados")

    if supermercado == "Todos":
        ranking = (
            df_filtrado.groupby("Supermercado")["Precio_Num"]
            .mean()
            .sort_values()
            .reset_index()
        )

        ranking.columns = [
            "Supermercado",
            "Promedio de Precio",
        ]

        ranking.index = ranking.index + 1

        ranking_tabla = ranking.reset_index()

        ranking_tabla.columns = [
            "Posición",
            "Supermercado",
            "Promedio de Precio",
        ]

        ranking_tabla["Promedio de Precio"] = (
            ranking_tabla["Promedio de Precio"].round(0).astype(int)
        )

        st.dataframe(
            ranking_tabla,
            use_container_width=True,
            hide_index=True,
        )

        ganador = ranking.iloc[0]

        st.success(
            f"Supermercado más económico: "
            f"{ganador['Supermercado']} "
            f"(Promedio: ${ganador['Promedio de Precio']:,.0f})"
        )

    else:
        st.info("Seleccione 'Todos' los supermercados para visualizar el ranking.")

# =====================================================
# DESCARGA DE DATOS
# =====================================================

st.header("Descargar resultados")

st.caption(
    "Los siguientes archivos corresponden a los resultados generales generados por el sistema."
)

# =====================================================
# FILA 1
# =====================================================

col1, col2 = st.columns(2)

csv_productos = df.to_csv(index=False, sep=";").encode("utf-8-sig")

col1.download_button(
    "Base de datos completa",
    csv_productos,
    "productos_marcas.csv",
    "text/csv",
)

csv_comparacion = comparacion.to_csv(index=False, sep=";").encode("utf-8-sig")

col2.download_button(
    "Comparación general",
    csv_comparacion,
    "comparacion_precios.csv",
    "text/csv",
)

# =====================================================
# FILA 2
# =====================================================

col3, col4 = st.columns(2)

csv_anomalias = anomalias.to_csv(index=False, sep=";").encode("utf-8-sig")

col3.download_button(
    "Anomalías generales",
    csv_anomalias,
    "anomalias_detectadas.csv",
    "text/csv",
)

# Ranking

if supermercado == "Todos":
    ranking_descarga = (
        df_filtrado.groupby("Supermercado")["Precio_Num"]
        .mean()
        .sort_values()
        .reset_index()
    )

    ranking_descarga.columns = [
        "Supermercado",
        "Promedio de Precio",
    ]

    ranking_csv = ranking_descarga.to_csv(index=False, sep=";").encode("utf-8-sig")

    col4.download_button(
        "Ranking general",
        ranking_csv,
        "ranking_supermercados.csv",
        "text/csv",
    )

    st.subheader("Grafico general")

    with open(
        "data/grafico_ranking.png",
        "rb",
    ) as file:
        st.download_button(
            label="Gráfico general",
            data=file,
            file_name="grafico_ranking.png",
            mime="image/png",
        )

# =====================================================
# INFORMACIÓN FINAL
# =====================================================

st.divider()

st.info(
    f"""
    Productos mostrados: {len(df_filtrado):,}

    Marcas visibles: {df_filtrado["Marca"].nunique()}

    Supermercados visibles: {df_filtrado["Supermercado"].nunique()}

    Anomalías visibles: {len(df_filtrado[df_filtrado["Anomalia"]])}
    """
)
