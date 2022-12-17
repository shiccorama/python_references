# next() : get the next element
# iter() : make iterator for the iterable element

str = "hassan"
print(next(iter(str))) # h
print(next(iter(str))) # a
print(next(iter(str))) # s
print(next(iter(str))) # s
print(next(iter(str))) # a
print(next(iter(str))) # n

# generators use "yield" instead of "return"

def generator():
	yield 1
	yield 2
	yield 3
	yield 4

myGen = generator()

# now you can control the flow of the function by using next() :
print(next(myGen)) # 1
print(f"I can make anything in between the function as you can see")
print(next(myGen)) # 2
# and so on, I can interupt the function and continue again with next()
# note that generator can produce multiple return , not just on return as functions


# ________ Decorators or meta-programming ______
# decorators are high-order function which means a function that accept another
# functions as parameters.

def myDecorator(recall_function):
    def nestedFunction():
        print(f"you can add anything before the recall function")
        recall_function()
        print(f"after decorating your function")
    return nestedFunction

def addTwoValues(a,b):
	print(a+b)

getFunctionAfterDecoration = myDecorator(addTwoValues(4,6))  # 10

# now, you can use decorator function without the need to use variables like this:
# also, you can use arguments inside wrapper function :

from functools import wraps
def outer_decorator(recall_function):
    @wraps(recall_function)
    def wrapper(*args, **kwargs):
        recall_function(*args, **kwargs)
        print(f"after decorating your function")
    return wrapper

@outer_decorator
def sayhi(name, age):
    print(f"hi my {name}, you're age {age}")

sayhi("love",32)


# you can use more than one decorator per one function :
# be aware that decorators will be executed as your arrangement:
# note : you need to add *args and **kwargs to nestedFunction before
# running the next function :

@myDecorator
@outer_decorator
def sayhi(name, age):
    print(f"hi my {name}, you're age {age}")

sayhi("hero",66)

# how to get the time of the running function :

from time import time

def speedTest(recall):
    def wrapper(*args, **kwargs):
        start = time()
        recall()
        end = time()
        print(f"actual time is : {end - start}")
    return wrapper

@speedTest
def longloop():
    range_ring = range(0,7000)
    for item in range_ring:
        print(f"{item}")

longloop()