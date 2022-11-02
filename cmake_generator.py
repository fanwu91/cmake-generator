import os 

cmake_minimum_requied = 'cmake_minimum_required(VERSION 3.16.5)'
project = 'project(master)'
include_directories = set()
glob_recurse = 'file(GLOB_RECURSE SRC_KERNEL *.c)'
add_executable = 'add_executable(master ${SRC_KERNEL})'

LINE_BREAK = '\n'
CMakeListsTxt = 'CMakeLists.txt'

def scan_dir(url):
    file  = os.listdir(url)
    for f in file:
        fpath = os.path.join(url, f)

        if (os.path.isfile(fpath) and fpath.endswith('.h')):
            include_directories.add(url)

        if (os.path.isdir(fpath)):
            if (f == 'include'):
                include_directories.add(fpath)
            scan_dir(fpath)

def create_cmake_file():
    result = ''
    result += cmake_minimum_requied + LINE_BREAK
    result += project + LINE_BREAK
    
    for dir in include_directories:
        result += 'include_directories(' + dir + ')' + LINE_BREAK
    
    result += glob_recurse + LINE_BREAK
    result += add_executable + LINE_BREAK

    return result

scan_dir('./')

if os.path.exists(CMakeListsTxt):
    os.remove(CMakeListsTxt)
file = open(CMakeListsTxt, 'w')
file.write(create_cmake_file())
file.close()
