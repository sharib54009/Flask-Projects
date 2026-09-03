import streamlit as st
import plotly.express as px
import pandas as pd

#Add title
st.title("In search for happiness")

#Add two select boxes

option_x = st.selectbox("Select the data for the x axis, ", ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data for the y axis, ", ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]
        
st.subheader(f"Scatter plot of {option_x} vs {option_y}")

figure1 = px.scatter(x=x_array, y=y_array, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure1)