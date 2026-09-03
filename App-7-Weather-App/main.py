import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next days")
place = st.text_input("Enter the name of the city")
days = st.slider("Select the number of days", min_value=1, max_value=5, help="Select the number of days for which you want to see the weather forecast")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [20, 22, 21]
    temperature = [days * i for i in temperatures]
    return dates, temperature


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (°C)"})
st.plotly_chart(figure)
