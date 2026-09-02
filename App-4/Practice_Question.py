import pandas as pd
import glob
import pathlib as path
from fpdf import FPDF

filepaths = glob.glob("Text-Files/*.txt")

for filepath in filepaths:
    df = pd.read_csv(filepath)
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    filename = path.Path(filepath).stem
    Header = filename
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'{Header}', ln=1)
   
    
    with open(filepath, 'r') as file:
        content = file.read()
       
    pdf.set_font(family='Times', size=10)
    pdf.multi_cell(w=0, h=8, txt=content)
    
    pdf.output(f"Text-Files/{filename}.pdf")