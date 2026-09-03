import streamlit as st
import plotly.express as px
import pandas as pd

#Add title
st.title("In search for happiness")

#Add two select boxes

option_x = st.selectbox("Select the data for the x axis, ", ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data for the y axis, ", ("GDP", "Happiness", "Generosity"))
