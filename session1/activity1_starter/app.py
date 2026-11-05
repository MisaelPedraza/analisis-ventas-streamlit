from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Ventas diarias", page_icon="📊", layout="wide")

CSV_PATH = Path(__file__).resolve().parents[2] / "sales_daily.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de datos: {CSV_PATH}. "
            "Ejecuta `python make_data.py` primero."
        )

    data = pd.read_csv(CSV_PATH, parse_dates=["date"])
    required_columns = {
        "date",
        "region",
        "category",
        "sku",
        "units",
        "revenue",
    }
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Faltan columnas requeridas en el CSV: {missing}")
    return data


st.title("Dashboard de ventas diarias")

try:
    df = load_data()
except (FileNotFoundError, ValueError) as error:
    st.error(str(error))
    st.stop()

with st.sidebar:
    st.header("Filtros")
    selected_regions = st.multiselect(
        "Región",
        options=sorted(df["region"].unique()),
        default=sorted(df["region"].unique()),
    )
    selected_categories = st.multiselect(
        "Categoría",
        options=sorted(df["category"].unique()),
        default=sorted(df["category"].unique()),
    )

filtered_df = df[
    df["region"].isin(selected_regions)
    & df["category"].isin(selected_categories)
]

st.subheader("Unidades diarias")
daily_units = (
    filtered_df.groupby("date", as_index=False)["units"]
    .sum()
    .sort_values("date")
)
units_chart = px.line(
    daily_units,
    x="date",
    y="units",
    markers=True,
    labels={"date": "Fecha", "units": "Unidades"},
)
st.plotly_chart(units_chart, use_container_width=True)

total_units = int(filtered_df["units"].sum())
total_revenue = float(filtered_df["revenue"].sum())
sku_count = int(filtered_df["sku"].nunique())

units_col, revenue_col, sku_col = st.columns(3)
units_col.metric("Unidades", f"{total_units:,}")
revenue_col.metric("Ingresos", f"${total_revenue:,.2f}")
sku_col.metric("Número de SKUs", f"{sku_count:,}")

st.subheader("Top 10 SKUs por ingresos")
top_skus = (
    filtered_df.groupby("sku", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
    .head(10)
)
sku_chart = px.bar(
    top_skus.sort_values("revenue"),
    x="revenue",
    y="sku",
    orientation="h",
    labels={"revenue": "Ingresos", "sku": "SKU"},
)
st.plotly_chart(sku_chart, use_container_width=True)

with st.expander("Mostrar datos filtrados"):
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
