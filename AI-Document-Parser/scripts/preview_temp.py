import openpyxl
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

file_path = r"D:\Công việc\3. Dự án Sovigaz\2. Tài liệu phân tích và thiết kế\02. BRD & Template\Template báo cáo - BRD.xlsx"
wb = openpyxl.load_workbook(file_path, data_only=True)
sheet = wb["1.1 temp doanh thu"]

print("--- FIRST 20 ROWS OF 1.1 temp doanh thu ---")
for row in sheet.iter_rows(min_row=1, max_row=20, values_only=True):
    print(row[:15])
