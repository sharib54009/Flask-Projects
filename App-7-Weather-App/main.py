import streamlit as st
st.title("Weather forecast for the next days")
place = st.text_input("Enter the name of the city")
days = st.slider("Select the number of days", min_value=1, max_value=5, help="Select the number of days for which you want to see the weather forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky", "Wind", "Humidity", "Pressure"))
st.subheader(f"{option} for the next {days} days in {place}")