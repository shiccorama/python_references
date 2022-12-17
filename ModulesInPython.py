# import module name :
import random

# print all functions inside this module :
print(dir(random))

# note: when importing the whole module, you have to use its name before any function:
text = "hassan"
print(random.sample(text,3))
# outputs, which is random, ["s", "n", "a"], any three random characters

# import from module a specific function :
from random import randint

# use one of the functions:
print(randint(100,120))
# random integer between 100 and 120

# to add your modules to system path to be able to use it :
import sys
sys.path.append(r"give it the path of your modules")
print(sys.path)  # check if your path is added

# you can use aliases for modules import :
import random as rr 
print(dir(rr))

# add alias for function imported :
from random import randint as rd
print(rd(1,9))

# you can add your own module path to vs code setttings.json:
"python.autoComplete.extraPaths" : ["D:\\python\\myModules"]

# packages are a set of modules combined can be downloaded by PIP
# PIP is python package manager as gem for ruby or npm for nodejs
# pip install packages and its dependencies 
# module list >>> "https:"//docs.python.org/3/py-modindex.html"
# packages and modules directories >>> "https://pypi.org/"
# to update pip:     pip install --user pip --upgrade

pip install pyfiglet
pip install termcolor

import pyfiglet, termcolor
print(termcolor.colored(pyfiglet.figlet_format("yourName"), color="yellow"))

# import datetime
# import strftime from datetime
# used to format time and date into strings
# you can check strftime.org for python directories.