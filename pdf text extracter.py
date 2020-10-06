import PyPDF2
from PackageHimaloy import *

user_input = int(input("Page number: "))
user_input = user_input - 1
reader = PyPDF2.PdfFileReader('Files/Biology.pdf')
text = reader.getPage(user_input).extractText()
createfile('Extracted text', text)
print("Done check your Desktop")
