import PyPDF2
from PackageHimaloy import *
from plyer import notification

reader = PyPDF2.PdfFileReader('Files/Biology.pdf')
text = ""
for page_number in range(reader.getNumPages()):
    text += reader.getPage(page_number).extractText()
createfile('Extracted text', text)

if __name__ == '__main__':
    notification.notify(
        title="A File has been created",
        message="A File Named Extracted text has been created CHECK YOUR DESKTOP!!",
        app_icon="images/glassofwater.ico",
        timeout=10
    )