import PyPDF2

# creating an object
file = open('/home/jario/Documentos/ENEM - 1998 à 2017/(1998) ENEM/1998 - ENEM - Prova amarela.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
print(fileReader.numPages)

print(fileReader.getPage(0).extractText())
