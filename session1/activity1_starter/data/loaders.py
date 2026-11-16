"""Carga y limpieza de ventas, independiente de la interfaz."""
from pathlib import Path

import pandas as pd
import streamlit as st

CSV_PATH = Path(__file__).resolve().parents[3] / "sales_daily.csv"


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina duplicados y unidades negativas; calcula revenue consistente."""
    clean = df.drop_duplicates().copy()
    clean = clean.loc[clean["units"] >= 0].copy()
    clean["revenue"] = (clean["units"] * clean["unit_price"]).round(2)
    return clean.reset_index(drop=True)


@st.cache_data(show_spinner="Cargando ventas...")
def load_sales(path: str | None = None) -> pd.DataFrame:
    """Lee y limpia el CSV una vez; cachea el resultado entre recargas."""
    source = Path(path) if path is not None else CSV_PATH
    return clean_sales(pd.read_csv(source, parse_dates=["date"]))
