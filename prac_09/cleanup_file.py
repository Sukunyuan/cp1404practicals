"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main() :
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for filename in os.listdir('.') :
        if os.path.isdir(filename) :
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename) :
    """Return a 'fixed' version of filename."""
    CharList = []
    if " " in filename:
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
        return new_name
    else:
        for n, char in enumerate(filename):
            if n == 0:
                char.upper()
            elif n > 0:
                if char.isupper() is True:
                    CharList.append("_")
            CharList.append(char)
        new_name = "".join(CharList)
        return new_name


def demo_walk() :
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.') :
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


main()
