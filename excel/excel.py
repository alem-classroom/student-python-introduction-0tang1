import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
# type(wb)
print(wb.sheetnames)
sheet = wb['Лист1']
print(sheet)
print(sheet.title)
