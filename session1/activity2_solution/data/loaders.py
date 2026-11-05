"""Data loading and cleaning helpers for the sales dashboard."""
from pathlib import Path

import pandas as pd
import streamlit as st


DEFAULT_PATH = Path(__file__).resolve().parents[3] / "sales_daily.csv"


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows and recalculate revenue from valid units."""
    out = df.drop_duplicates().copy()
    out = out[out["units"] >= 0]
    out["revenue"] = (out["units"] * out["unit_price"]).round(2)
    return out.reset_index(drop=True)


@st.cache_data(show_spinner="Loading sales...")
def load_sales(path: str | None = None) -> pd.DataFrame:
    """Load and clean the sales CSV."""
    csv_path = Path(path) if path else DEFAULT_PATH
    return clean_sales(pd.read_csv(csv_path, parse_dates=["date"]))
