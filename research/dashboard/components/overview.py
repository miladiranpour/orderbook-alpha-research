import streamlit as st


def show_overview(metadata):
    columns = st.columns(3)

    columns[0].metric("Market", metadata.get("market", "BTC/USDT"))
    columns[1].metric("Horizon", f"{metadata.get('horizon', 'N/A')} sec")
    columns[2].metric("Records", metadata.get("records", "N/A"))
