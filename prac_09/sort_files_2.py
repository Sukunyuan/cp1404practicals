import os
import shutil


os.chdir('FilesToSort')
for directory, subdirectories, filenames in os.walk("."):
    file_dic = {}
    file_list = []
    for file in filenames:
        file_style = file.split(".")[1]
        if file_style not in file_dic:
            dir_style = input("What category would you like to sort {} files into? ".format(file_style))
            file_dic[file_style] = dir_style
            if dir_style not in file_list:
                os.mkdir(dir_style)
                file_list.append(dir_style)
        shutil.move(file, file_dic[file_style])
