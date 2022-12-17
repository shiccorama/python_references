# to determine if all elements in an iterable elment are True
all(iterable_element)

# to determine if at least in an iterable elment are True
any(iterable_element)

# to convert any number to binary
bin(number)

# to know the reference location of a variable
a = 18
id(d)  # 1243982740923748723

# sum(iterable, number to add)
sum()
# round(number, no. of digits)
round()
# range(start, end, step) -- end is the default value
# range also doesn't contain the end number
range(12) # 12 here is the end, means (0 : 12)
a = list(range(2,10,2))
print(a)
# print more than one value with specific separator
print("how", "are", "you", sep="@")
#  how@are@you
# print function has default end as "n", you can alter it :
print("how", "are", "you", end="\t\t")
print("hassa mohamed")
# how are you   hassan mohamed

# abs() : outputs absolute value of -ve numbers
print(abs(-33))  # 33
# pow(base, exponential, mod) : outputs the power
print(2,5)  # 32
# min() # gets values or iterators (list, tuple, ..)
print(min('z', 'x', 'salem')) # salem becasue of "s"
# max() # gets values or iterators 
print(max('z', 'x', 'salem'))  # "z"
  
# slice() === a[start, end, step]
a = [1,2,3,4,5,6]
print(a[slice(2,4)])  # [3,4]



#__________________ map(function, iterator)____________________
# map function ( can take function and iterators as params)
# first define the function that you want to iterate over the iterators
def sayHello(name):
	return f"Hello my dear {name}"

# the iterator :
myTuple = ("ahmed", "ali", "hassan")

# save the output in variable "data" :
data = map(sayHello, myTuple)

print(type(data))  # <class "map">
print(data)  # <map object at 0x7f12kk3k3k>

for item in data:
	print(item)
# hello my dear ahmed
# hello my dear ali
# hello my dear hassan

# map(lambda function, iterator)
for name in list(map(lambda text: f"lambda function :{text.strip().capitalize()}", myTuple)):
	print(name)
# output : lambda function :Ahmed, lambda function :Ali, lambda function : Hassan

#__________________ filter(function, iterator)____________________
# return True values only which achieved the condition.

def checkValue(num):
	return num>10

numList = [33,2,4,12,44,56,2,3]

filteredList = filter(checkValue, numList)
print(type(filteredList))  # <class "filter">

for n in filteredList:
	print(n)  # 33,12,44,56

# filter(lambda funtion, tuple)

name_list = ("said", "morgan", "hassan", "hany")
names_filter = filter((lambda name : name.startswith("h")), name_list)
for item in names_filter:
	print(item)  # hassan, hany

	#__________________ reduce(function, iterator)____________________
# reduce function can only be used after importing from functools module
# from functools import reduce
# reduce takes first and second arguments and combine a result, this result
# will be combined with 3rd argument and returns result and this result will
# be combined with 4th, and so on....

from functools import reduce

least_list = [18,44,77,13,34,56,32]

def leastNum(n,m):
	if n < m :
		return n
	else :
		return m

reduced_num = reduce(leastNum, least_list)
print(reduced_num)  # 13

# let's try it in lambda function with ternary operator :

min_num = reduce((lambda n,m : n if n < m else m ),least_list)
print(min_num)   # 13

# ______ enumerate( iterable, start = 0) ______
# used to add counter to your list, tuple :

skills = ["html", "css", "js", "python"]
enum_skills = enumerate(skills, 100)

for skill in enum_skills:
	print(skill)
# (100, "html")
# (101, "css")
# (102, "js")
# (103, "python")

print(type(enum_skills))   # < class "enumerate" >

for count, skill in enum_skills:
	print(f"{count} === {skill}")

# 100 === html
# 101 === css
# 102 === js
# 103 === python


# ______ help() ______
# help function will provide you with manual 

print(help(min))  # manual for min function

# ______ reversed(iterable) ______

skills = ["html", "css", "js", "python"]
reversed_skills = reversed(skills)
for i in reversed_skills:
  print(i)  # python, js, css, html

