import streamlit as st


def show_ranking(ranking):
    st.header("Feature Ranking")
    st.dataframe(ranking, width="stretch", hide_index=True)
