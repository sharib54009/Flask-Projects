import streamlit as st
import plotly.express as px
from Backend import get_data

#Add Title, text_input , slide, header, subheader
st.title("Weather forecast for the next days")
place = st.text_input("Enter the name of the city")
days = st.slider("Select the number of days", min_value=1, max_value=5,
                help="Select the number of days for which you want to see the weather forecast")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
  
#Get the temperature/sky
filtered_data = get_data(place, days)

if option == "Temperature":
        figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (°C)"})
        st.plotly_chart(figure)
        
if option == "Sky":
    
