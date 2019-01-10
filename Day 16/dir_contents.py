import os

mylist = os.listdir()

for file_or_dir in mylist:
    if (os.path.isdir(file_or_dir)):
        print("FOLDER:", end="")

    if (os.path.isfile(file_or_dir)):
        print("FILE:", end="")

    print (" " + file_or_dir)