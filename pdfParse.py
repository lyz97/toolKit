import pandas as pd
import pdfplumber
import pandas as pd
import numpy as np


def pdf_load(path):
    with pdfplumber.open(path) as pdf:
        first_page = pdf.pages[54]
        # first_page = first_page.dedupe_chars(tolerance=1)
        content = first_page.dedupe_chars().extract_tables()
        mylist = pd.DataFrame(content)
        mylist[1, :].to_csv('result.csv', encoding='utf_8_sig')
        print(mylist)


if __name__ == '__main__':
    pdf_path = 'C:/Users/31192/Desktop/决策知识模型/决策知识模型参考资料/21-QRH.pdf'
    pdf_load(pdf_path)
