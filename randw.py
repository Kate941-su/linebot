import xlrd
import pprint

wb=xlrd.open_workbook("planandday1.xls")#open xls file(wb=work book)
ws = wb.sheet_by_name('plan')#get sheet data(ws=work sheet)
cell = ws.cell(1,2)
print(cell)
print(cell.value)

print(ws.col(0))#get col data
print(ws.row(0))#get row data
col_end=len(ws.col(0))
row_end=len(ws.row(0))

print(col_end,row_end)
latest_id=ws.cell(col_end-1,row_end-1).value
latest_id=int(latest_id)#cast float -> int
print(latest_id)#get latest id

wb=xlrd.open_workbook("planandday1.xls")
ws = wb.sheet_by_name('plan')
row_end=len(ws.row(0))
col_end=len(ws.col(0))
latest_row=ws.cell(col_end-1,row_end-2).value
latest_row=int(latest_row)#cast float -> int
