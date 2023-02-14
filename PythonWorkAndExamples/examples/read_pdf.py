# importing required modules
import PyPDF2
# from PyPDF2 import PdfReader

# creating a pdf reader object
reader = PyPDF2.PdfFileReader('/home/jitendra/Downloads/sample.pdf')

# # printing number of pages in pdf file
page = reader.getNumPages()
print("page", page)
#
# # get document information
# text = reader.documentInfo
# print("text", text)
# print("get page detail", reader.getPage().getContents())

str = ""
for i in range(page):
    str += reader.getPage(i).extractText()
print("str", str)