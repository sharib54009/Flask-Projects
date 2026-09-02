import requests
import streamlit as st

api_key = "Co6MahU8X8t7kizZAZFBXLhnThjppWAqsF66F8dW"

url = "https://api.nasa.gov/planetary/apod?" \
    f"api_key={api_key}"

response1 = requests.get(url)
data = response1.json()


title = data["title"]
image_url = data["url"]
description = data["explanation"]

image = requests.get(image_url)

with open("nasa.jpg", "wb") as f:
    f.write(image.content)

st.title(title)
st.image("nasa.jpg", caption=title, use_column_width=True)
st.write(description)    
    
    
    
    
