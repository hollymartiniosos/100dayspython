from PyPDF2 import PdfReader
import pyttsx3

path = open('test.pdf', 'rb')

pdfReader = PdfReader(path)

from_page = pdfReader.pages[0]

text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()