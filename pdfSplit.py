
from PyPDF2 import PdfFileWriter, PdfFileReader


def pdf_split(pdf_in, pdf_out, start, end):
    # 初始化一个pdf
    output = PdfFileWriter()
    # 读取pdf
    with open(pdf_in, 'rb') as in_pdf:
        pdf_file = PdfFileReader(in_pdf)
        # 从pdf中取出指定页
        for i in range(start, end):
            output.addPage(pdf_file.getPage(i))
        # 写出pdf
        output.removeLinks()  # 去掉所有链接
        with open(pdf_out, 'ab') as out_pdf:
            output.write(out_pdf)


def pdf_merge(merge_list, output_pdf):
    """
    merge_list: 需要合并的pdf列表
    output_pdf：合并之后的pdf名
    """
    # 实例一个 PDF文件编写器
    output = PdfFileWriter()
    for ml in merge_list:
        pdf_input = PdfFileReader(open(ml, 'rb'))
        page_count = pdf_input.getNumPages()
        for i in range(page_count):
            output.addPage(pdf_input.getPage(i))

    output.write(open(output_pdf, 'wb'))


if __name__ == '__main__':
    """
    文件输出后，如果没有删除直接再次运行输出文件，会导致文件过大。
    """

    # pdf_in = 'C:/Users/31192/Desktop/DO-200B.PDF'
    # pdf_out = 'C:/Users/31192/Desktop/111111.pdf'
    #
    # # 拆分的起始位置和结束位置 开始的页码需要减1，如从第1页第30页，起始为0, 30
    # s, e = 98, 78
    # pdf_split(pdf_in, pdf_out, s, e)  # 插入代码片

    merge_list = ['1', '2_1', '2_2', '3', '4', '5', '6']

    merge_list = ['C:/Users/31192/Desktop/答辩材料打印版/' + x + '.pdf' for x in merge_list]

    pdf_merge(merge_list, 'C:/Users/31192/Desktop/答辩材料打印版/需要打印的.pdf')
