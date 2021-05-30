import pyttsx3
import PyPDF2
book = open('python.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
page = pdfReader.numPages
print(page)
speaker = pyttsx3.init()
speaker.say('Hello Guys i am Python audible')
for num in range( 0, page):
 page = pdfReader.getPage(5)
text = page.extractText()
speaker.say(text)
speaker.say('Thank you guys for listing to me')
speaker.runAndWait()