import streamlit as st

st.title("Weather Forecast for next 5 days")
place = st.text_input("Enter the place name")

days = st.slider("Select the number of days for forecast", min_value=1, max_value=5, help="Select the number of days for which you want to see the weather forecast")

option = st.selectbox("Select Data to view", ("temperature", "Sky"))

st,st.subheader(f"{option} for next {days} days in {place}")