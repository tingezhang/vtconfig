

import model
import sys
import model_reader as reader
import model_writer as writer
import svg_generator as generator
import xterm_256_gen


def __printUsage():
    print sys.argv[0], 'input xls', 'output xls', 'output svg'
    sys.exit(1)



def findMostLikeColor(color_str, xterm_256_colorset):
    idx = 0
    distance = 0
    mostlikecolor_str = 0

    r_int = int(color_str[0:2], 16)
    g_int = int(color_str[2:4], 16)
    b_int = int(color_str[4:6], 16)

    for color_grp in xterm_256_colorset.grp:
        for color_row in color_grp.row:
            for color_cell in color_row.cell:
                org_color_str = color_cell.fill
                r_int_org = int(org_color_str[0:2], 16)
                g_int_org = int(org_color_str[2:4], 16)
                b_int_org = int(org_color_str[4:6], 16)

                local_distance = pow((r_int - r_int_org), 2) + pow((g_int - g_int_org), 2) + pow((b_int - b_int_org), 2)
                if 0 == distance:
                    distance = local_distance
                    idx = color_cell.idx
                    mostlikecolor_str = org_color_str
                elif local_distance <  distance :
                    distance = local_distance
                    idx = color_cell.idx
                    mostlikecolor_str = org_color_str

    return idx, mostlikecolor_str


def main():
    if len(sys.argv) < 4:
        __printUsage()

    xterm_256_colorset = xterm_256_gen.gen_xterm256_colorset()

    input_xls_file = sys.argv[1]
    output_xls_file = sys.argv[2]
    output_svg_file = sys.argv[3]

    color_set = reader.load_model(input_xls_file)
    added_grp_list = []

    for color_grp in color_set.grp:
        added_grp = model.ColorGrp(color_grp.name + '_vim')
        added_grp.width = color_grp.width
        added_grp.height = color_grp.height

        for color_row in color_grp.row :
            added_row = model.ColorRow(color_row.row)
            added_row.width = color_row.width
            added_row.height = color_row.width

            for color_cell in color_row.cell:
                added_cell = model.ColorCell(color_cell.col, color_cell.idx,
                            color_cell.fill, color_cell.width, color_cell.height,
                            color_cell.text, color_cell.textColor)
                added_cell.idx, added_cell.fill = findMostLikeColor(added_cell.fill, xterm_256_colorset)
                added_row.cell.append(added_cell)

            added_grp.row.append(added_row)

        added_grp_list.append(added_grp)

    for added_grp in added_grp_list:
        color_set.grp.append(added_grp)
        color_set.height += added_grp.height

    writer.store_model(output_xls_file, color_set)
    generator.render_set(color_set, output_svg_file)

if '__main__' == __name__:
    main()


