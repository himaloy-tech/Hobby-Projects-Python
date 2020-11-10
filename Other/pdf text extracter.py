import PyPDF2
from PackageHimaloy import *
from plyer import notification

user_input = int(input("Page number: "))
user_input = user_input - 1
reader = PyPDF2.PdfFileReader('Files/Biology.pdf')
text = reader.getPage(user_input).extractText()
createfile('Extracted text', text)
if __name__ == '__main__':
    notification.notify(
        title=f"A File has been created",
        message="A File Named Extracted text has been created CHECK YOUR DESKTOP!!",
        app_icon="images/glassofwater.ico",
        timeout=10
    )