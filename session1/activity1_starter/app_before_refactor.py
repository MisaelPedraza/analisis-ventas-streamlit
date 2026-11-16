"""Activity 1: interactive sales explorer based on the starter kit."""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA = Path(__file__).resolve().parents[2] / "sales_daily.csv"

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")

if not DATA.exists():
    st.error(f"No se encontró el archivo de datos: {DATA}")
    st.stop()

df = pd.read_csv(DATA, parse_dates=["date"])

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

daily = filtered_df.groupby("date", as_index=False)["units"].sum()
fig = px.line(daily, x="date", y="units", title="Daily units")
st.plotly_chart(fig, width="stretch")

units_col, revenue_col, sku_col = st.columns(3)
units_col.metric("Total units", f"{filtered_df['units'].sum():,.0f}")
revenue_col.metric("Revenue", f"${filtered_df['revenue'].sum():,.2f}")
sku_col.metric("# SKUs", f"{filtered_df['sku'].nunique():,}")

st.subheader("Top 10 SKUs by revenue")
top_skus = (
    filtered_df.groupby("sku", as_index=False)["revenue"]
    .sum()
    .nlargest(10, "revenue")
    .sort_values("revenue")
)
sku_fig = px.bar(
    top_skus,
    x="revenue",
    y="sku",
    orientation="h",
    labels={"revenue": "Revenue", "sku": "SKU"},
)
st.plotly_chart(sku_fig, width="stretch")

with st.expander("Show filtered rows"):
    st.dataframe(filtered_df, width="stretch", hide_index=True)
