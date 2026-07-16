from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from research.dashboard.components.overview import show_overview
from research.dashboard.components.metrics import show_metrics
from research.dashboard.components.probability import show_probability
from research.dashboard.components.ranking import show_ranking
from research.dashboard.loader import load_result
from research.dashboard.presenter import ResearchPresenter


RESULT_PATH = Path("results/latest.pkl")


st.set_page_config(page_title="OrderBook Alpha", layout="wide")
st.title("OrderBook Alpha Research Dashboard")

if not RESULT_PATH.exists():
    st.error("Research result not found. Run main.py to create results/latest.pkl.")
    st.stop()

presenter = ResearchPresenter(load_result(RESULT_PATH))

show_overview(presenter.overview())
show_ranking(presenter.ranking())
show_metrics(presenter.metrics())
show_probability(presenter.analyses())
