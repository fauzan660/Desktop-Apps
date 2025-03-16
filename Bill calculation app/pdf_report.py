import webbrowser
from fpdf import FPDF

class Pdfreport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.image("housing.jpg", x=0, y=0, w=600, h=900)

        pdf.set_font(family="Times", size=38, style="B")
        pdf.cell( w=0, h=80, txt="Flatmates Bill", align="C", border=0, ln=1)

        pdf.set_font(family="Times", size=25, style="B")
        pdf.cell(w=110, h=40, txt=" Period", border=0, align="C")
        pdf.cell(w=180, h=40, txt=bill.period, border=0, align="C", ln=0)

        pdf.cell(w= 100, h=40, align= "C", border=0,txt = flatmate1.name)
        pdf.cell(w= 150, h=40, align= "C", border=0,txt = str(round(flatmate1.pays(bill, flatmate2.days_in_house), 2)) + " $", ln=1)


        pdf.set_font(family="Times", size=20)
        pdf.cell(w=100, h=40, align="C", border=0, txt=flatmate2.name)
        pdf.cell(w=150, h=40, align="C", border=0, txt=str(round(flatmate2.pays(bill, flatmate1.days_in_house), 2)) + " $", ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)
