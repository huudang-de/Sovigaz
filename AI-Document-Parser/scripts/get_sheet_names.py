import openpyxl
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

file_path = r"D:\Công việc\3. Dự án Sovigaz\2. Tài liệu phân tích và thiết kế\02. BRD & Template\Template báo cáo - BRD.xlsx"
wb = openpyxl.load_workbook(file_path, data_only=True)
print("Các sheet có trong file:")
for name in wb.sheetnames:
    print(f"- '{name}'")
