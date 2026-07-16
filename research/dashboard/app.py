from pathlib import Path

import streamlit as st

from research.dashboard.loader import load_result
from research.dashboard.presenter import ResearchPresenter


RESULT_PATH = Path("results/latest.pkl")


st.set_page_config(page_title="OrderBook Alpha", layout="wide")
st.title("OrderBook Alpha Research Dashboard")

if not RESULT_PATH.exists():
    st.error("Research result not found. Run main.py to create results/latest.pkl.")
    st.stop()

presenter = ResearchPresenter(load_result(RESULT_PATH))

overview = presenter.overview()
overview_columns = st.columns(3)
overview_columns[0].metric("Market", overview["market"])
overview_columns[1].metric("Horizon", f"{overview['horizon'] or 'N/A'} sec")
overview_columns[2].metric("Rows", overview["records"] or "N/A")

st.header("Feature Ranking")
st.dataframe(presenter.ranking(), use_container_width=True, hide_index=True)

st.header("Metrics")
st.dataframe(presenter.metrics(), use_container_width=True, hide_index=True)
