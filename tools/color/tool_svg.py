import sys
import model_reader as reader
import svg_generator as generator
import model
import model_writer as writer
import xterm_256_gen as gen256


def test():
    #color_set = reader.load_model('xterm_256.xls')
    color_set = gen256.gen_xterm256_colorset()

    print color_set
    reader.dump_model(color_set)
    generator.render_set(color_set, 'output.svg')

    writer.store_model('tmp_out_2.xls', color_set)

def __printUsage():
    print sys.argv[0], 'xls_model_file', 'out_svg_file'
    sys.exit(0)

if '__main__' == __name__:
    if len(sys.argv) < 3:
        __printUsage()

    xls_filename = sys.argv[1]
    svg_filename = sys.argv[2]

    color_set = reader.load_model(xls_filename)
    generator.render_set(color_set, svg_filename)


