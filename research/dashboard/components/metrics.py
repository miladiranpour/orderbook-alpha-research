import plotly.express as px
import streamlit as st


def show_metrics(metrics):
    st.header("Feature Metrics Comparison")

    metric = st.selectbox(
        "Select Metric",
        ["Correlation", "Average Return", "Win Rate", "Sharpe"],
    )

    chart_data = metrics.sort_values(by=metric, ascending=False)
    figure = px.bar(
        chart_data,
        x="Feature",
        y=metric,
        title=f"{metric} Comparison",
    )

    st.plotly_chart(figure, width="stretch")
