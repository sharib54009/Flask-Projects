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
 
if place:  
    
    try:
        #Get the temperature/sky
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"]/10 for dict in filtered_data] 
            dates = [dict["dt_txt"] for dict in filtered_data]
            #Plot the temperature
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (°C)"})
            st.plotly_chart(figure)
                
        if option == "Sky":
            images = {"Clouds":"images/cloud.png", "Clear":"images/clear.png",
                    "Rain":"images/rain.png", "Snow":"images/snow.png "}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data] 
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width = 115)
    except:
        st.write("That place does not exists")
