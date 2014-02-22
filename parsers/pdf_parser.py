import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

def main():
    pagenos = set()
    password = ''
    maxpages = 0
    # output option
    # outfile = 'parsed.txt'
    imagewriter = None
    rotation = 0
    layoutmode = 'normal'
    codec = 'utf-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()
    rsrcmgr = PDFResourceManager(caching=caching)
    # outfp = sys.stdout
    outfp = file('parsed.txt', 'w')
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,imagewriter=imagewriter)
    fp = file("../Certificates.pdf", 'rb')
    # first throw the pdf contents into a text
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos,
                                      maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    outfp.close()
    print("things")
    # second open the text file, and pull out the columns
    parsed = open('parsed.txt', 'rb')
    row_to_skip = 5
    columns = 13
    row = 0
    column = 0
    for line in parsed:
    	print row
    	if (row >= row_to_skip):
    		print line
    	row += 1

if __name__ == "__main__":
    sys.exit(main())