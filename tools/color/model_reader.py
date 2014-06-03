
import xlrd
import model

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

def dump_model(color_set):
    print 'set name', color_set.name
    print 'width', color_set.width
    print 'height', color_set.height

    for color_grp in color_set.grp:
        print '\tgrp name', color_grp.name
        print '\twidth', color_grp.width
        print '\theight', color_grp.height

        for color_row in color_grp.row :
            print '\t\trow idx', color_row.row
            print '\t\twidth', color_row.width
            print '\t\theight', color_row.height

            for color_cell in color_row.cell:
                content = ['\t\t\t']
                content.append('col'); content.append(str(color_cell.col))
                content.append('idx'); content.append(str(color_cell.idx))
                content.append('fill'); content.append(color_cell.fill)
                content.append('width'); content.append(str(color_cell.width))
                content.append('height'); content.append(str(color_cell.height))
                content.append('text'); content.append(color_cell.text)
                content.append('textColor'); content.append(color_cell.textColor)
                print ",".join(content)


def load_model(filename):
    wb = xlrd.open_workbook(filename)

    color_set = model.ColorSet(filename)

    menu_sheet = wb.sheet_by_name('GroupList')

    set_width = 0
    set_height = 0
    for row in range(menu_sheet.nrows):
        if 0 == row:
            continue
        name = menu_sheet.cell(row, 0).value
        width = int(menu_sheet.cell(row, 1).value)
        height = int(menu_sheet.cell(row, 2).value)
        color_grp = model.ColorGrp(name)
        color_grp.width = width
        color_grp.height = height

        color_set.grp.append(color_grp)

        sheet = wb.sheet_by_name(name)
        for n in range(sheet.nrows):
            if 0 == n:
                continue

            row_num = int(sheet.cell_value(n, 0))
            col_num = int(sheet.cell_value(n, 1))
            idx     = int(sheet.cell_value(n, 2))
            fill    = _getCellString(sheet.cell(n, 3))
            width   = int(sheet.cell_value(n, 4))
            height  = int(sheet.cell_value(n, 5))
            text    = _getCellString(sheet.cell(n, 6))
            textCol = _getCellString(sheet.cell(n, 7))

            try:
                color_row = color_grp.row[row_num]
            except IndexError:
                color_row = model.ColorRow(row_num)
                color_grp.row.insert(row_num, color_row)

            color_cell = model.ColorCell(col_num, idx, fill, width, height, text, textCol)
            color_row.cell.insert(col_num, color_cell)

        grp_width = 0
        grp_height = 0
        for color_row in color_grp.row:
            row_width = 0
            row_height = 0

            for color_cell in color_row.cell:
                row_width += color_cell.width;
                if row_height < color_cell.height:
                    row_height = color_cell.height

            color_row.width = row_width
            color_row.height = row_height

            grp_height += row_height
            if grp_width < row_width:
                grp_width = row_width

        if color_grp.width < grp_width:
            color_grp.width = grp_width
        if color_grp.height < grp_height:
            color_grp.height = grp_height

        set_height += color_grp.height
        if set_width < color_grp.width:
            set_width = color_grp.width

    color_set.width = set_width
    color_set.height = set_height
    return color_set
