import xlrd,xlwt
import openpyxl
import pprint
from random import randint
wb=xlrd.open_workbook("planandday1.xlsx")#open xls file(wb=work book)
ws = wb.sheet_by_name('plan')#get sheet data(ws=work sheet)
cell = ws.cell(1,2)
print(cell)
print(cell.value)

col_end=ws.ncols
row_end=ws.nrows

print(ws.col(0))

print(col_end,row_end)
latest_id=ws.cell(row_end-1,col_end-1).value
latest_id=int(latest_id)#cast float -> int
print(latest_id)#get latest id

wb=xlrd.open_workbook("planandday1.xlsx")
ws = wb.sheet_by_name('plan')
row_end=len(ws.row(0))
col_end=len(ws.col(0))
buffer_col=7
latest_row=ws.cell(col_end-1,row_end-2).value
latest_row=int(latest_row)#cast float -> int
print(latest_row)
issue_id=randint(0,10000)

wb=openpyxl.load_workbook("planandday1.xlsx")
ws=wb.worksheets[0]
ws.cell(row=latest_row+1,column=buffer_col,value="sample")
wb.save("planandday1.xlsx")