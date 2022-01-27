from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import os
import pandas as pd

def read_pdf(file_name):
    output_string = StringIO()
    with open(file_name, "rb") as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return output_string.getvalue()

info = pd.read_csv(rf"/Users/hoonjo/Documents/pdf/info.csv",encoding="euc-kr", usecols=["사번", "이름", "주민번호"])
info_list = []
for i in info.itertuples():
    number = i[1]
    name = i[2]
    jumin = i[3]
    set = str(number)+str(name)+str(jumin)
    info_list.append(set)

file_name_check = "file_list"
file_name_list = os.listdir(file_name_check)

for i in file_name_list:
    try:
        txt = read_pdf(rf"/Users/hoonjo/Documents/pdf/file_list/{i}")
        name_jumin = txt[80:149]
        name_jumin_edit = name_jumin.strip()
        name = name_jumin_edit[5:10]
        name_edit = name.replace(" ","")
        name_edit = name_edit.strip("\n")
        jumin = name_jumin_edit[-14:]
        value = jumin[0:6]
        value = value.strip("\n")
        name_jumin_value = str(name_edit)+str(value)
        
        for b in info_list:
            if name_jumin_value in b:
                print(f"경진여객{b}")
                befor = (rf"/Users/hoonjo/Documents/pdf/file_list/{i}")
                after = (rf"/Users/hoonjo/Documents/pdf/after_file_list/경진여객{b}.pdf")
                os.rename(befor, after)

    except:
        print(f"error_{i}")