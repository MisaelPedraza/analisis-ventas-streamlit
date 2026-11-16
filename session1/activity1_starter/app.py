"""Activity 2: modular Sales Explorer. Solo interfaz, filtros, KPIs y composición."""
import streamlit as st

from components.charts import daily_units_chart, top_skus_chart
from data.loaders import load_sales

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")

try:
    df = load_sales()
except (FileNotFoundError, OSError, ValueError) as exc:
    st.error(f"No se pudieron cargar los datos de ventas: {exc}")
    st.stop()

with st.sidebar:
    st.header("Filtros")
    selected_regions = st.multiselect(
        "Región",
        options=sorted(df["region"].unique()),
        default=sorted(df["region"].unique()),
        key="sales_regions",
    )
    selected_categories = st.multiselect(
        "Categoría",
        options=sorted(df["category"].unique()),
        default=sorted(df["category"].unique()),
        key="sales_categories",
    )

filtered_df = df[
    df["region"].isin(selected_regions)
    & df["category"].isin(selected_categories)
]

if filtered_df.empty:
    st.warning("No hay ventas para estos filtros. Selecciona al menos una región y una categoría.")
    st.stop()

st.plotly_chart(daily_units_chart(filtered_df), width="stretch")

units_col, revenue_col, sku_col = st.columns(3)
units_col.metric("Total units", f"{filtered_df['units'].sum():,.0f}")
revenue_col.metric("Revenue", f"${filtered_df['revenue'].sum():,.2f}")
sku_col.metric("# SKUs", f"{filtered_df['sku'].nunique():,}")

st.subheader("Top 10 SKUs by revenue")
st.plotly_chart(top_skus_chart(filtered_df), width="stretch")

with st.expander("Show filtered rows"):
    st.dataframe(filtered_df, width="stretch", hide_index=True)
