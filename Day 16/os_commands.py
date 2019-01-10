import os

print("We start here")
print (os.getcwd())

#os.chdir('C:\\Users\\1835069\\Pychar')

os.chdir("test_dir")
print(os.getcwd())

f = open("new file2", "w")
f.write("Hello")