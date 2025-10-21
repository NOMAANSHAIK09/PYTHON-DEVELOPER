# imported all  package
import streamlit as st
import plotly.express as px
import pandas as pd
# tittle 
st.title("In Search for Happiness")
# two selectboxes have three option 
option_x = st.selectbox("Select the data for the X-axis",
                      ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data for the Y-axis",
                      ("GDP", "Happiness", "Generosity"))
# used pandas to get data from file 
df = pd.read_csv("happy.csv")
#set x_array varible none
x_array = None
# used match cases if option select is a the extract a from file
match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]
#set x_array varible none
y_array = None
# used match cases if option select is a the extract a from file
match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]
# header 
st.subheader(f"{option_x} and {option_y}")
# figure to plot graph
figure1 = px.line_3d(x=x_array, y=y_array, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure1)
