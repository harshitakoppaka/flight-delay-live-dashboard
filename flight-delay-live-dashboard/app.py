import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Flight Delay Dashboard", layout="wide")

st.title("Flight Delay Analysis Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("flights.csv")

df = load_data()

st.sidebar.header("Filter Options")
airline = st.sidebar.selectbox("Select Airline", df["airline"].unique())

filtered_df = df[df["airline"] == airline]

st.subheader("Summary Statistics")

col1, col2 = st.columns(2)
col1.metric("Average Departure Delay", round(filtered_df["dep_delay"].mean(), 2))
col2.metric("Average Arrival Delay", round(filtered_df["arr_delay"].mean(), 2))

st.subheader("Departure Delay Distribution")

fig, ax = plt.subplots()
sns.histplot(filtered_df["dep_delay"], kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Top Delayed Flights")
st.dataframe(filtered_df.sort_values("dep_delay", ascending=False))
