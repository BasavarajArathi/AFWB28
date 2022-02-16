#READING DATA FROM EXCEL
import openpyxl

#1. open the excel file(workbook)
wb=openpyxl.load_workbook("F:/B28/Book1.xlsx")
#2. goto required sheet
sheet1=wb['Sheet1']
#3. get the value present in required cell
v=sheet1.cell(1,1).value
#4. print the value
print(v)
#5. close the xl file
wb.close()
