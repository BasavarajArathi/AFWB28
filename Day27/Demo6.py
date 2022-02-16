#WRITING DATA FROM EXCEL
import openpyxl

wb=openpyxl.load_workbook("F:/B28/Book1.xlsx")
sheet1=wb['Sheet1']
sheet1.cell(1,1).value="Bhanu"
wb.save("F:/B28/Book1.xlsx")
wb.close()

