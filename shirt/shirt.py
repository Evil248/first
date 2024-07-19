import sys
from PIL import Image, ImageOps
from os.path import splitext
def main():
    check_command_line_arg()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirtfile = Image.open("shirt.png")
    size = shirtfile.size
    muppet = ImageOps.fit(imagefile, size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])
def check_command_line_arg():
    if len(sys.argv) <3:
        sys.exit("Too tew command-line arguments")
    if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_exten(file1[1]) == False:
        sys.exit("Invalid input")
    if check_exten(file2[1]) == False:
        sys.exit("Invalid input")
    if  file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions ")
def  check_exten(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False
main()
