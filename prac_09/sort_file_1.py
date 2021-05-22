import os
import shutil

os.chdir("FilesToSort")
for directory, subdirectories, filenames in os.walk("."):
    for file in filenames:
        end_name = file.split(".")[1]
        try:
            os.mkdir(end_name)
        except FileExistsError:
            pass
        shutil.move(file, end_name)