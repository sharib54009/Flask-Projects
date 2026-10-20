import pandas as pd
from fpdf import FPDF
from streamlit import pdf


df = pd.read_csv('articles.csv', dtype = {'id' : str})



class Stock:
    
    def __init__(self, stock_id):
        self.stock_id = stock_id
    
    def buy(self):
        self.article = df.loc[df['id'] == self.stock_id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.stock_id, 'price'].squeeze()
        
        df.loc[df['id'] == self.stock_id, 'in stock'] = df.loc[df['id'] == self.stock_id, 'in stock'] - 1
        try:
            df.to_csv('articles.csv', index=False)
            print("Stock bought successfully!")
        except PermissionError:
            print("Cannot save the CSV file. Close Excel or check file permissions.")
        pass
    
    
class Generate_pdf:
    
    def __init__(self):
        pass
    
    def generate_pdf(self, article, price):
        
       
        
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.1", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {article}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {price}", ln=1)

        pdf.output("receipt.pdf")

        pass
    
print(df)

Stock_id = input("enter Stock if to buy")
stock = Stock(Stock_id)

stock.buy()

generate_pdf = Generate_pdf()
generate_pdf.generate_pdf(stock.article, stock.price)
