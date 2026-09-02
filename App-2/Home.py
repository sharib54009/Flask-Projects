import streamlit as st
import pandas as pd

st.set_page_config(page_title="About Me", page_icon=":smiley:", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Photo.jpg", width=300, )

with col2:
    st.title("Mohammed Sharib")
    content = """
              Iam a software developer with a passion for creating innovative solutions. With a strong background in programming and problem-solving, I enjoy tackling complex challenges and delivering high-quality results. I am constantly learning and staying up-to-date with the latest technologies to enhance my skills and contribute to impactful projects.
              """
    st.info(content)
    
    
content2 = """
Below you can find the apps i have built using python . feel free to contact me 
"""

st.write(content2)

col3, col4 = st.columns(2)


df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=200)
        st.markdown(f"[Source Code]({row['url']})")
    
with col4:
    for index, row in df.iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=200)
        st.markdown(f"[Source Code]({row['url']})")