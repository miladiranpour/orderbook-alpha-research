import plotly.express as px
import streamlit as st


def show_probability(analysis):
    st.header("Probability Analysis")

    features = list(analysis.keys())
    if not features:
        st.info("No probability analysis is available.")
        return

    feature = st.sidebar.selectbox(
        "Probability Feature",
        features,
        key="probability_feature",
    )
    probability = analysis[feature].get("Probability")

    if probability is None or probability.empty:
        st.info(f"No probability data is available for {feature}.")
        return

    st.subheader(f"{feature} Probability")
    st.dataframe(probability, width="stretch", hide_index=True)

    if len(probability.columns) < 2:
        return

    probability_column = probability.columns[-1]
    probabilities = probability[probability_column].dropna()
    monotonic = probabilities.is_monotonic_increasing
    st.metric("Monotonic UP Probability", "Yes" if monotonic else "No")

    figure = px.bar(
        probability,
        x=probability.columns[0],
        y=probability_column,
        title=f"{feature} - UP Probability",
    )
    st.plotly_chart(figure, width="stretch")
