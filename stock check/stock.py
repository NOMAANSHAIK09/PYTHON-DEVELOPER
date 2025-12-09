from fpdf import FPDF
import pandas as pd

df = pd.read_csv(r"c:/python/hotel booking aap/stock check/articles.csv",dtype={"id": str})

class Article:
    def __init__(self,article_id):
        self.id=article_id
        self.name=df.loc[df['id']==self.id,'name'].squeeze()
        self.price=df.loc[df['id']==self.id,'price'].squeeze()

    def available(self):
        in_stock=df.loc[df['id']==self.id,'in stock'].squeeze()
        print(in_stock)
        return in_stock
        
        

class Recipt:
    def __init__(self,article):
        self.article=article
    def generate(self):
        pdf=FPDF(orientation="p",unit="mm",format="A4")
        pdf.add_page()

        pdf.set_font(family="Times",size=16,style="B")
        pdf.cell(w=50,h=8,txt=f"recipt nr.{self.article.id}",ln=1)

        pdf.set_font(family="Times",size=16,style="B")
        pdf.cell(w=50,h=8,txt=f"article:{self.article.name}",ln=1)

        pdf.set_font(family="Times",size=16,style="B")
        pdf.cell(w=50,h=8,txt=f"prize{self.article.price}",ln=1)

        pdf.output("recpit.pdf")
        print("✔ Receipt generated: receipt.pdf")



print(df)
article_id=input("chose any stock id :")
article=Article(article_id=article_id)
if article.available():
    recipt=Recipt(article)
    recipt.generate()
else:
    print("no such article")
