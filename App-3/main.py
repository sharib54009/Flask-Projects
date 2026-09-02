from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto= False, margin = 0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
     for i in range(row["Pages"] ):
         
        #ADDS HEADER
        pdf.add_page()
        pdf.set_font(family="Arial", style="B", size=12)
        pdf.set_text_color(77, 33, 120)
        pdf.cell(w=0, h=12, txt=row["Topic"],  align="L")
        pdf.line(10, 20, 200, 20)     
        
        #ADDS FOOTER        
        pdf.ln(265)
        pdf.set_font(family="Arial", style="I", size=6)
        pdf.set_text_color(77, 33, 120)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")    
        
        for y in range(20, 270, 10):
            pdf.line(10, y , 200, y)   
        
     
pdf.output("output.pdf")

