"""
Packages To Be Installed

1. pip install pyttsx3
2. pip install PyPDF2

"""
import pyttsx3
import PyPDF2
book = open("""Enter PDF File Name Saved In Folder""", "rb")
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range("""Enter Page No""", pages):
    page = pdfreader.getPage("""Enter Page No""")
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()