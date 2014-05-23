#!/usr/bin/env python
'''
usage
python config_vim.py -f PATH_TO_FILE -t PATH_TO_TYPE
PATH_TO_FILE: source file search path, one path a line
PATH_TO_TYPE: source file name pattern need to cared about, one pattern a line
'''
import sys
import os

dir_file_name = ''
file_type_name = ''

def print_usage():
    print("====================== USAGE =======================\n")
    print("python config_vim.py -f PATH_TO_FILE -t PATH_TO_TYPE\n")
    print("PATH_TO_FILE: source file search path, one path a line\n")
    print("PATH_TO_TYPE: source file name pattern need to cared about, one pattern a line\n")



def analysis_param():
    global dir_file_name
    global file_type_name

    if 5 != len(sys.argv):
        print(sys.argv)
        print_usage()
        return 0

    if sys.argv[1] != "-f" or sys.argv[3] != "-t":
        print_usage()
        return 0

    if '/' == sys.argv[2][0] :
        dir_file_name = sys.argv[2]
    else:
        dir_file_name = os.getcwd() + "/" +  sys.argv[2]

    if '/' == sys.argv[4][0]:
        file_type_name = sys.argv[4]
    else:
        file_type_name = os.getcwd() + "/" + sys.argv[4]

    if not os.path.isfile(dir_file_name) or not os.path.isfile(file_type_name) :
        print_usage()
        return 0

    return 1


def main():
    if not analysis_param() :
        return

    dirStr = ''
    fileTypeStr = ''
    searchPathStr = ''
    print("dir_file_name: " + dir_file_name);
    print("file_type_name: " + file_type_name);
    fFile = open(dir_file_name,'r')
    count = 0
    for line in fFile:
        dirStr += ' ' + line.strip('\n')
        if 0 == count:
            if line.endswith('/'):
                searchPathStr += line.strip('\n') + "**"
            else:
                searchPathStr += line.strip('\n') + "/**"
        else:
            if dirStr.endswith('/'):
                searchPathStr += ',' + line.strip('\n') + "**"
            else:
                searchPathStr += ',' + line.strip('\n') + "/**"

        count = count + 1

    fFile.close()

    fFile = open(file_type_name, 'r')
    count = 0
    for line in fFile :
        if 0 == count :
            fileTypeStr += " -name \"" + line.strip('\n') + "\""
        else :
            fileTypeStr += " -o -name \"" + line.strip('\n') + "\""
        count = count + 1

    fFile.close()


    print("find " + dirStr + fileTypeStr + " > files.sc \n")
    os.system("find " + dirStr + fileTypeStr + " > files.sc")

    print("ctags -R --c++-kinds=+p --fields=+iaS --extra=+q -L files.sc \n")
    os.system("ctags -R --c++-kinds=+p --fields=+iaS --extra=+q -L files.sc")

    print("cscope -Rbq -i files.sc \n")
    os.system("cscope -Rbq -i files.sc")

    print("echo -e \'!_TAG_FILE_SORTED\\t2\\t/2=foldcase/\' > filenametags\n")
    fFile = open("./filenametags", 'w')
    fFile.write("!_TAG_FILE_SORTED\t2\t/2=foldcase/\n")
    fFile.close()

    print("find " + dirStr + " -not -regex \'.*\\.\\(png\\|gif\\)\' -type f -printf \"%f\\t%p\\t1\\n\" | sort -f >> filenametags")
    os.system("find " + dirStr + " -not -regex \'.*\\.\\(png\\|gif\\)\' -type f -printf \"%f\\t%p\\t1\\n\" | sort -f >> filenametags")

    print("cp ~/.vimrc .")
    os.system("cp ~/.vimrc .")

    fFile = open(".vimrc", "a")
    print("echo \"\\n:set path+=" + searchPathStr + "\\n\" >> .vimrc")
    fFile.write("\n:set path+=" + searchPathStr + "\n")

    print("echo \":let g:LookupFile_TagExpr = \'\"./filenametags\"\'\"\\n >> .vimrc")
    fFile.write(":let g:LookupFile_TagExpr = \'\"./filenametags\"\'\n")

    print("echo \":cs add cscope.out\\n\" >> .vimrc")
    fFile.write("\n:cs add cscope.out\n")
    fFile.close()


main()






