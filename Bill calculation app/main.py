
from pdf_report import Pdfreport
from flatmate_and_bill import Flatmate, Bill


mate1 = input("What is the name of flatmate 1: ").capitalize()
mate2 = input("What is the name of flatmate 2: ").capitalize()

month = input("Which month's bill is this: ").capitalize()
tbill = int(input("What is the total bill this month: "))
m1_days = int(input(f"How many days did {mate1.capitalize()} live in the house "))
m2_days = int(input(f"How many days did {mate2.capitalize()} live in the house "))



the_bill = Bill(tbill, month)
m1 = Flatmate(mate1, m1_days)
m2 = Flatmate(mate2, m2_days)
file1 = Pdfreport(filename= "test_report_1.pdf")
file1.generate(flatmate1= m1, flatmate2= m2, bill= the_bill)
