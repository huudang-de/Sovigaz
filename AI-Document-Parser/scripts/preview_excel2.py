import openpyxl
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

file_path = r"D:\Công việc\3. Dự án Sovigaz\2. Tài liệu phân tích và thiết kế\02. BRD & Template\Template báo cáo - BRD.xlsx"
wb = openpyxl.load_workbook(file_path, data_only=True)
sheet = wb["1.BRD- DOANH THU"]

print("--- ROWS 16 TO 35 ---")
for row in sheet.iter_rows(min_row=16, max_row=35, values_only=True):
    # Only print rows that have at least one non-None value to keep output clean
    if any(cell is not None for cell in row):
        print(row[:15]) # Print first 15 columns to avoid too much text
