
import model


def _render_cell(x, y, color_cell):
    width = color_cell.width
    height = color_cell.height
    fill = color_cell.fill
    idx = color_cell.idx
    text = color_cell.text
    textColor = color_cell.textColor


    content = '<g transform=\"translate(' + str(x) +', ' + str(y) +')\">'
    content += '<rect x=\"0\" y=\"0\" width=\"' + str(width) + '\" height=\"' + str(height) + '\" style=\"fill:#' + fill +';\"/>'
    content += '<text x=\"40\" y=\"32\" style=\"fill:#'+ textColor + ';text-anchor:middle;\">'+fill +'</text>'
    content += '<text x=\"2\" y=\"57\" style=\"fill:#' + textColor + ';\">' + str(idx) + '</text>'
    content += '</g>'
    return content

def _render_row(x, y, color_row):
    content = ''

    for color_cell in color_row.cell:
        content += _render_cell(x, y, color_cell) + '\n'


        x += color_cell.width

    return content


def _render_grp(x, y, color_grp):
    content = ''

    for color_row in color_grp.row:
        content += _render_row(x, y, color_row) + '\n'
        y += color_row.cell[0].height

    return content

def render_set(color_set, output):
    content = ''
    width = color_set.width
    height = color_set.height
    x = 0
    y = 0

    ofile = open(output, 'w')
    content += '<svg xmlns=\"http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink\" version=\"1.1\" width=\"'+str(width) +'\" height=\"' + str(height) +'\">\n'
    content += '<style>text {font-size:9pt;font-family: \"Bitstream Vera Sans Mono\", \"Droid Sans Mono\", \"Menlo\", \"Monaco\", \"Consolas\", \"Inconsolata\", \"Courier New\";fill: white; }</style>'
    content += '<rect x=\"0\" y=\"0\" width=\"' + str(width) +'\" height=\"' + str(height) + '\" style=\"fill:black\"/>'

    ofile.write(content)
 
    for color_grp in color_set.grp:
        content = _render_grp(x, y, color_grp)
        y += color_grp.row[0].cell[0].height * len(color_grp.row)
        ofile.write(content)

    content= '</svg>'
    ofile.write(content);
    ofile.close()

