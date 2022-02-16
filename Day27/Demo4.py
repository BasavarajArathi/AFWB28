#READING DATA FROM EXCEL
import openpyxl

wb=openpyxl.load_workbook("F:/B28/Book1.xlsx")

sheet1=wb['Sheet1']

for i in range(1,4):
    for j in range(1,4):
        v=sheet1.cell(i,j).value
        print(v,end=" ")
    print()
wb.close()

#A1 B1  C1
#A2 B2  C2
#A3 B3  C3