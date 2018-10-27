import os, shutil, re
import PyPDF2
from datetime import datetime
curdir = "C:\\Users\\GLAMKE\\Desktop\\Downloads"
for file in os.listdir(curdir):
    if "Print_Certificate" in file:
        file = os.path.join(curdir, file)   #use a full path filename
        # print(file)
        with open(file, "rb") as pdf_obj:
            read_pdf = PyPDF2.PdfFileReader(pdf_obj)
            page = read_pdf.getPage(0)
            extracted = page.extractText()
            # print(extracted)
            if "ARRS" in extracted:
                title = (re.findall('"(.+)"', extracted)[0])
                journal = "ARRS"
                date = datetime.now().strftime("%Y%m%d")
                credit = (re.findall('\d.\d\d', extracted)[0])
            new_filename = "{} {} {} {}.pdf".format(date, journal, credit, title)        
            print(new_filename)
        new_filename =  os.path.join(curdir, new_filename)  # Do I want to put them in another folder?  
        shutil.copy2(file, new_filename)
        