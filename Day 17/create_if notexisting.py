import os

dirname = "TestDir"

def create_dir_ifnotexsiting(name):

    if not os.path.isdir(name):
        os.mkdir(name)
        print("Directory " + name + " created.")
    else:
        print("The supplied name is  direcory that already exists")

create_dir_ifnotexsiting("abc")