import streamlit as st
import pandas


st.set_page_config(layout="wide")



col_1, col_2 = st.columns(2)

with col_1:
    st.image("images/NomanAbbas.jpg",width=400)

    
with col_2:
    st.title("Noman Abbas")
    content = """
    Hi, I am Noman Abbas! I am a Python programmer, Network Security Engineer, and founder of TechnologyHub. I graduated in 2016 with a Bachlor of Science in Computer Science from Government College University Faisalabad Pakistan.
    I have worked with companies from various countries, such as the Center for Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
    """
    st.info(content)
    
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)


col_3,dmpty_col,col_4 = st.columns([1.5,0.5,3.5])

df = pandas.read_csv("data.csv", sep=";")

with col_3:
    for index, row in df[:12].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
        
with col_4:
    for index, row in df[12:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
    
    