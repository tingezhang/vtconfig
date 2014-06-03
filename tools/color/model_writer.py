
import xlwt
import model



def store_model(filename, color_set):
    wb = xlwt.Workbook()
    menu_sheet = wb.add_sheet('GroupList')

    menu_sheet.write(0, 0, 'GroupName')
    menu_sheet.write(0, 1, 'ItemWidth')
    menu_sheet.write(0, 2, 'ItemHeight')

    cnt = 1
    for color_grp in color_set.grp :
        menu_sheet.write(cnt, 0, color_grp.name)
        menu_sheet.write(cnt, 1, 80)
        menu_sheet.write(cnt, 2, 60)
        cnt += 1

        sheet = wb.add_sheet(color_grp.name)
        sheet.write(0, 0, 'Row')
        sheet.write(0, 1, 'Column')
        sheet.write(0, 2, 'Index')
        sheet.write(0, 3, 'Fill')
        sheet.write(0, 4, 'Width')
        sheet.write(0, 5, 'Height')
        sheet.write(0, 6, 'Text')
        sheet.write(0, 7, 'TextCol')

        cnt_line = 1
        for color_row in color_grp.row:
            row_num = color_row.row
            for color_cell in color_row.cell:
                col_num = color_cell.col
                idx = color_cell.idx
                fill = color_cell.fill
                width = color_cell.width
                height = color_cell.height
                text = color_cell.text
                textColor = color_cell.textColor

                sheet.write(cnt_line, 0, row_num)
                sheet.write(cnt_line, 1, col_num)
                sheet.write(cnt_line, 2, idx)
                sheet.write(cnt_line, 3, fill)
                sheet.write(cnt_line, 4, width)
                sheet.write(cnt_line, 5, height)
                sheet.write(cnt_line, 6, text)
                sheet.write(cnt_line, 7, textColor)

                cnt_line += 1

    wb.save(filename)















