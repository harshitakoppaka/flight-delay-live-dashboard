import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page configuration
st.set_page_config(
    page_title="Flight Delay Dashboard",
    layout="wide"
)

st.title("✈️ Flight Delay Analysis Dashboard")
st.markdown("Interactive exploration of airline delay patterns.")

# Load data safely for local + cloud deployment
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "flights.csv")
    return pd.read_csv(file_path)

df = load_data()

# Sidebar filter
st.sidebar.header("Filter Options")
airline = st.sidebar.selectbox(
    "Select Airline",
    df["airline"].unique()
)

filtered_df = df[df["airline"] == airline]

# Metrics
st.subheader("Summary Statistics")

col1, col2 = st.columns(2)

col1.metric(
    "Average Departure Delay (min)",
    round(filtered_df["dep_delay"].mean(), 2)
)

col2.metric(
    "Average Arrival Delay (min)",
    round(filtered_df["arr_delay"].mean(), 2)
)

# Chart
st.subheader("Departure Delay Distribution")

fig, ax = plt.subplots()
sns.histplot(filtered_df["dep_delay"], kde=True, ax=ax)
ax.set_xlabel("Departure Delay (minutes)")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Data Table
st.subheader("Top Delayed Flights")

top_delays = filtered_df.sort_values(
    by="dep_delay",
    ascending=False
)

st.dataframe(top_delays, use_container_width=True)
