
import xlrd

def _getCellString(cell):
    value = ''
    if xlrd.XL_CELL_EMPTY == cell.ctype :
        value = ''
    elif xlrd.XL_CELL_TEXT == cell.ctype :
        value = cell.value
    elif xlrd.XL_CELL_NUMBER == cell.ctype :
        value = str(int(cell.value))
    elif xlrd.XL_CELL_DATE == cell.ctype:
        value = str(cell.value)
    elif xlrd.XL_CELL_BOOLEAN == cell.ctype:
        value = str(cell.value)
    elif xlrd.XL_CELL_ERROR == cell.ctype:
        value = str(cell.value)
    elif xlrd.XL_CELL_BLANK == cell.ctype:
        value = cell.value
    else :
        print 'unrecoginized type'
        value = ''
    return value


wb = xlrd.open_workbook("xterm_256.xls")

for s in wb.sheets():
    print 'Sheet:', s.name
    print s.nrows
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols) :
            values.append(_getCellString(s.cell(row, col)))
        print ','.join(values)
    print


