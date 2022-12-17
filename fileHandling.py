# file handling #

# "a" == Append "open file for appending values or create file if it doesn't exist"
# "r" == Read "open file for reading and gives error if file doesn't exist"
## note: open() will open file with (read) as default value .
# "w" == Write "open file for writing or create file if it doesn't exist"
# "x" == Create "create file and gives error if the file already exists"

import os   # get some commands from os library

print(os.getcwd())    # get current working directory, to know which folder you're working at

print(os.path.abspath(__file__))  # will print the absolute path of the current file

print(os.path.dirname(os.path.abspath(__file__)))  # directory path for opened file

print(os.chdir(os.path.dirname(os.path.abspath(__file__))))  # if you want to change directory

print

file = open()  # (read) by default

# if you have folder named as "nfiles", when you try to get its absolute path
# it will give an error , like this :

file = open("D:\Python\Files\nfiles\function.py")

# so, to make python reads this file correctly , you need to add "r" before the path

file = open(r"D:\Python\Files\nfiles\function.py")

print(file)  # file data object and not the content
print(file.name)  # function.py
print(file.mode)  # reading mode by default
print(file.encoding) # encoding characters used

print(file.read())  # this will read the content of the file, if you didn't give params

print(file.readline()) # read line by line, you can give params for lines

print(file.readlines()) # this will output <list> with all lines, you can iterate over them

for line in file:  # loop through lines in file
	print(line)
	if line.startswith("some characters you know")  # stop the loop at certain point
	break

# it's preferable to close the connection or the file after using it :
file.close()

## write and append :

newFile = open(r"D:\python\test.txt", "w") # note: we added the mode as "w" == write
## first thing's first : if file doesn't exist, "w" will create it
## second : write will always overwrite the content, so, if you've some lines, "w" will overwrite it

newFile.write("this is the first line")
newFile.write("this is the second line") 
# note: the two lines will be side by side because you didn't use ("\n")
# output: this is the first linethis is the second line
newFile.write("this is the 2nd line\n")
newFile.write("this is the 3rd line") 
newFile.write("this is 1000 repeated sentences\n" * 1000)
myList = [1"\n",2"\n",3"\n",4"\n",5"\n"]
newFile.writelines(myList) # this will iterate over the list and print all
newFile.close()

# open file to append :
newFile = open(r"D:\python\test.txt", "a")
# append will add line without overwriting any .
# please be careful of the cursor's position and new line \n
newFile.truncate(5) # will truncate 5 characters and remove the rest
# for example : "imagination is perfect" will be "imagi"

# remove file after import os :
os.remove(r"D:/python/file.txt")