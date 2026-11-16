"""Constructores de figuras Plotly reutilizables, sin llamadas a Streamlit."""
import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure


def daily_units_chart(df: pd.DataFrame) -> Figure:
    """Misma serie diaria que la app original."""
    daily = df.groupby("date", as_index=False)["units"].sum()
    return px.line(daily, x="date", y="units", title="Daily units")


def top_skus_chart(df: pd.DataFrame) -> Figure:
    """Mismas barras horizontales y orden que la app original."""
    top = (
        df.groupby("sku", as_index=False)["revenue"]
        .sum()
        .nlargest(10, "revenue")
        .sort_values("revenue")
    )
    return px.bar(
        top, x="revenue", y="sku", orientation="h",
        labels={"revenue": "Revenue", "sku": "SKU"},
    )
