from openpyxl import load_workbook
import os
xlsx_name_list=next(os.walk('.'))[2]  #获取当前文件下所有文件
# print(xlsx_name_list)

wb=load_workbook()