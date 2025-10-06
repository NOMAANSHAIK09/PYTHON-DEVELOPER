import streamlit
from fpdf import FPDF
import pandas as pd

df=pd.read_csv("topics.csv")

pdf = FPDF(orientation="p",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index,row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Times", style="B" , size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)

    for y in range(20,295,10):   
        pdf.line(10,y,200,y)

    #set footer 
    pdf.ln(265)
    pdf.set_font(family="Times",style="I",size=10)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0 , h= 10 , txt=row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()
         #set footer 
        pdf.ln(266)
        pdf.set_font(family="Times",style="I",size=10)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0 , h= 10 , txt=row["Topic"], align="R")
        for y in range(20,295,10):   
            pdf.line(10,y,200,y)


pdf.output("output.pdf")