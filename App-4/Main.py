from sqlite3 import Date

import pandas as pd
import glob
from fpdf import FPDF
import pathlib as path

filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    
    
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    
    
    filename = path.Path(filepath).stem 
    invoice_nr, Date = filename.split('-')
    
    
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice nr. {invoice_nr}', ln=1)
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Date: {Date}', ln=1)
    
    
    df = pd.read_excel(filepath)
    
    #Add Header
    columns = list(df.columns)
    columns = [item.replace('_', ' ').title() for item in columns]
    pdf.set_font(family='Times', size=10, style='B')
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=50, h=8, txt=columns[1], border=1)
    pdf.cell(w=50, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    
    
    
    
    #Add Rows
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=50, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=50, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)
    
    
    total_price = df['total_price'].sum()
    pdf.set_font(family='Times', size=10)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), border=1, ln=1)    
        
    
    
    #Add Total sum sentence
    pdf.set_font(family='Times', size=10, style='B')
    pdf.cell(w=30, h=8, txt=f"Total Amount: {total_price:.2f}", ln=1)
    
    
    pdf.output(f"PDFs/{filename}.pdf")
    