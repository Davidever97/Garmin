from fpdf import FPDF
from datetime import datetime, timedelta
pdf = FPDF()
today= datetime.today()
today=today.date()
today1 =today - timedelta(days=30) 
width=210
km= 217
d=2000
def create_title(pdf):
  # Unicode is not yet supported in the py3k version; use windows-1252 standard font
  pdf.set_font('Arial', '', 20)  
  pdf.ln(60)
  pdf.write(5, f"Activtity Report, powered by Garmin and Python")
  pdf.ln(10)
  pdf.set_font('Arial', '', 16)
  pdf.write(4, f'From {today1} to {today}')
  pdf.ln(5)


# First Page 
pdf.add_page()
pdf.image("/Users/davideesposito/Desktop/Personali/Garmin/head.png", 0, 0,  width) #,w=0,h=0
create_title(pdf)
pdf.set_font('Arial', '', 15)   
pdf.ln(60)
pdf.write(3, f"The total km this month are: {km} km")
pdf.ln(10)
pdf.set_font('Arial', '', 15)   
pdf.write(3, f"The total elevation gain this month is: {d} m ")
pdf.ln(10)


pdf.output("/Users/davideesposito/Desktop/Personali/Garmin/report.pdf", 'F')
