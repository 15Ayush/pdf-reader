# importing required modules
import PyPDF2


def readPdf(pdf,N):

    # creating a pdf file object
    pdfFileObj = open(pdf, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(N)

    # extracting text from page
    return pageObj.extractText()

    # closing the pdf file object
    pdfFileObj.close()