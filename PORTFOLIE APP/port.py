import streamlit as st 
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("image/noman.jpg" )
    #st.write("nomaan")

with col2:
    st.title("NOMAAN SHAIK")
    contant ="""
         Hi, i am nomaan shaik! i am an frontend developer , and learning python developer .know i am persuing 
         artificital intaligens engeneering from methodist collage of engeneering and technolagy 
              """
    st.info(contant)
contant2="""Below are some app i bulit by using python"""
st.write(contant2)

col3,empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/"+ row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/"+ row["image"])
        st.write(f"[source code]({row['url']})")