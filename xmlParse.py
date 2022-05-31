# _*_coding=utf-8_*_
from xml.etree import ElementTree as ET
import pandas as pd
import numpy as np

# xml 地址
tree = ET.parse('path.xml')
root = tree.getroot()
label = []
error_label = []
file_label = []

operation_DataFrame = pd.DataFrame()
print(root.tag)
for child in root:
    # print(child.tag, child.attrib)
    if child.tag == 'scene':
        continue
    operation_list = {}
    for node in child:
        # ----------------------  -获取所有标签类型----------------------------
        if node.tag not in label:
            label.append(node.tag)
        if node.tag == 'error':
            for child_node in node:
                if child_node.tag not in error_label:
                    error_label.append(child_node.tag)
        if node.tag == 'file':
            for child_node in node:
                if child_node.tag not in file_label:
                    file_label.append(child_node.tag)
        operation_list[node.tag] = node.text
    operation_DataFrame = pd.concat([operation_DataFrame, pd.DataFrame(operation_list, index=[0])], axis=0)

# 输出csv的地址
operation_DataFrame.to_csv('path.csv', encoding='utf_8_sig', index=False)







