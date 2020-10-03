# importing required modules 
import PyPDF2
from tts import *
import pyttsx3   
# init function to get an engine instance for the speech synthesis  




# creating a pdf file object 
pdfFileObj = open('A Walk To Remember – Nicholas Spark ( PDFDrive ).pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print(pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(1) 

# extracting text from page 
#print(pageObj.extractText())
engine.say(pageObj.extractText())
engine.runAndWait()

# closing the pdf file object 
pdfFileObj.close() 
