
import model
import model_writer as writer
import sys

color_list=['00', '5F', '87', 'AF', 'D7', 'FF']

def gen_xterm256_colorset():
    color_set = model.ColorSet('xterm_256')

    # Color16 group
    color_grp_color16 = model.ColorGrp('Color16')
    color_row = model.ColorRow(0)
    cell_list = color_row.cell
    cell_list.append(model.ColorCell(0, 0, '000000', 80, 60, '#000000', 'FFFFFF'))
    cell_list.append(model.ColorCell(1, 1, '800000', 80, 60, '#800000', 'FFFFFF'))
    cell_list.append(model.ColorCell(2, 2, '008000', 80, 60, '#008000', 'FFFFFF'))
    cell_list.append(model.ColorCell(3, 3, '808000', 80, 60, '#808000', 'FFFFFF'))
    cell_list.append(model.ColorCell(4, 4, '000080', 80, 60, '#000080', 'FFFFFF'))
    cell_list.append(model.ColorCell(5, 5, '800080', 80, 60, '#800080', 'FFFFFF'))
    cell_list.append(model.ColorCell(6, 6, '008080', 80, 60, '#008080', 'FFFFFF'))
    cell_list.append(model.ColorCell(7, 7, 'C0C0C0', 80, 60, '#C0C0C0', 'FFFFFF'))
    color_row.width = 640
    color_row.height = 60
    color_grp_color16.row.append(color_row)

    color_row = model.ColorRow(1)
    cell_list = color_row.cell
    cell_list.append(model.ColorCell(0, 8, '808080', 80, 60, '#808080', '000000'))
    cell_list.append(model.ColorCell(1, 9, 'FF0000', 80, 60, '#FF0000', '000000'))
    cell_list.append(model.ColorCell(2, 10, '00FF00', 80, 60, '#00FF00', '000000'))
    cell_list.append(model.ColorCell(3, 11, 'FFFF00', 80, 60, '#FFFF00', '000000'))
    cell_list.append(model.ColorCell(4, 12, '0000FF', 80, 60, '#0000FF', '000000'))
    cell_list.append(model.ColorCell(5, 13, 'FF00FF', 80, 60, '#FF00FF', '000000'))
    cell_list.append(model.ColorCell(6, 14, '00FFFF', 80, 60, '#00FFFF', '000000'))
    cell_list.append(model.ColorCell(7, 15, 'FFFFFF', 80, 60, '#FFFFFF', '000000'))
    color_row.width = 640
    color_row.height = 60
    color_grp_color16.row.append(color_row)
    color_grp_color16.width = 640
    color_grp_color16.height = 120


    if color_set.width < color_grp_color16.width:
        color_set.width = color_grp_color16.width
    color_set.height += color_grp_color16.height

    color_set.grp.append(color_grp_color16)

    cnt = 16

    # red cube group
    for red in color_list:
        color_grp = model.ColorGrp('Red' + red)
        for r, green in enumerate(color_list):
            color_row = model.ColorRow(r)
            cell_list = color_row.cell
            if r < 3 :
                textCol = 'FFFFFF'
            else:
                textCol = '000000'

            for c, blue in enumerate(color_list):
                cell_list.append(model.ColorCell(c, cnt, red + green + blue, 80, 60, '#' + red + green + blue, textCol))
                cnt += 1
            color_row.width = len(color_list) * 80
            color_row.height = 60
            color_grp.row.append(color_row)
        color_grp.width = len(color_list) * 80
        color_grp.height = len(color_list) * 60

        if color_set.width < color_grp.width :
            color_set.width = color_grp.width
        color_set.height += color_grp.height
        color_set.grp.append(color_grp)

    # black/write group
    row = 0
    color_grp_blackWhite = model.ColorGrp('BlackWhite')
    color_row = model.ColorRow(row)
    cell_list = color_row.cell
    cell_list.append(model.ColorCell(0, cnt, '080808', 80, 60, '#080808', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(1, cnt, '121212', 80, 60, '#121212', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(2, cnt, '1C1C1C', 80, 60, '#1C1C1C', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(3, cnt, '262626', 80, 60, '#262626', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(4, cnt, '303030', 80, 60, '#303030', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(5, cnt, '3A3A3A', 80, 60, '#3A3A3A', 'FFFFFF')); cnt += 1
    color_row.width = 480
    color_row.height = 60
    color_grp_blackWhite.row.append(color_row)

    row += 1
    color_row = model.ColorRow(row)
    cell_list = color_row.cell
    cell_list.append(model.ColorCell(0, cnt, '444444', 80, 60, '#444444', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(1, cnt, '4E4E4E', 80, 60, '#4E4E4E', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(2, cnt, '585858', 80, 60, '#585858', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(3, cnt, '606060', 80, 60, '#606060', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(4, cnt, '666666', 80, 60, '#666666', 'FFFFFF')); cnt += 1
    cell_list.append(model.ColorCell(5, cnt, '767676', 80, 60, '#767676', 'FFFFFF')); cnt += 1
    color_row.width = 480
    color_row.height = 60
    color_grp_blackWhite.row.append(color_row)

    row += 1
    color_row = model.ColorRow(row)
    cell_list = color_row.cell
    cell_list.append(model.ColorCell(0, cnt, '808080', 80, 60, '#808080', '000000')); cnt += 1
    cell_list.append(model.ColorCell(1, cnt, '8A8A8A', 80, 60, '#8A8A8A', '000000')); cnt += 1
    cell_list.append(model.ColorCell(2, cnt, '949494', 80, 60, '#949494', '000000')); cnt += 1
    cell_list.append(model.ColorCell(3, cnt, '9E9E9E', 80, 60, '#9E9E9E', '000000')); cnt += 1
    cell_list.append(model.ColorCell(4, cnt, 'A8A8A8', 80, 60, '#A8A8A8', '000000')); cnt += 1
    cell_list.append(model.ColorCell(5, cnt, 'B2B2B2', 80, 60, '#B2B2B2', '000000')); cnt += 1
    color_row.width = 480
    color_row.height = 60
    color_grp_blackWhite.row.append(color_row)

    row += 1
    color_row = model.ColorRow(row)
    cell_list = color_row.cell
    cell_list.append(model.ColorCell(0, cnt, 'BCBCBC', 80, 60, '#BCBCBC', '000000')); cnt += 1
    cell_list.append(model.ColorCell(1, cnt, 'C6C6C6', 80, 60, '#C6C6C6', '000000')); cnt += 1
    cell_list.append(model.ColorCell(2, cnt, 'D0D0D0', 80, 60, '#D0D0D0', '000000')); cnt += 1
    cell_list.append(model.ColorCell(3, cnt, 'DADADA', 80, 60, '#DADADA', '000000')); cnt += 1
    cell_list.append(model.ColorCell(4, cnt, 'E4E4E4', 80, 60, '#E4E4E4', '000000')); cnt += 1
    cell_list.append(model.ColorCell(5, cnt, 'EEEEEE', 80, 60, '#EEEEEE', '000000')); cnt += 1
    color_row.width = 480
    color_row.height = 60
    color_grp_blackWhite.row.append(color_row)
    color_grp_blackWhite.width = 480
    color_grp_blackWhite.height = 240

    if color_set.width < color_grp_blackWhite.width:
        color_set.width = color_grp_blackWhite.width
    color_set.height += color_grp_blackWhite.height

    color_set.grp.append(color_grp_blackWhite)


    return color_set

def printUsage():
    print sys.argv[0], 'output_xls_file_name'
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        printUsage()

    filename = sys.argv[1]
    color_set = gen_xterm256_colorset()
    writer.store_model(filename, color_set)

if '__main__' == __name__:
    main()

