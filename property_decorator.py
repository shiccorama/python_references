# property decorator is using to change a function with self attribute only to attribute
# that is using by just calling its name without parenthesis () 
# in other words, instead of say print(say_hello()), we use print(say_hello)

class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello my dear {self.name}")


    @property
    def legal_age(self):
        if (self.age >= 18):
            print(f"Pass, you can enter the site")
        else :
            print(f"Sorry, you're not legal to enter the site")

# taking instance from class Test:

person = Test("Ahmed", 22)

person.say_hello() 
# hello my dear Ahmed
# person.legal_age() 
# "NoneType" object is not callable ( because you made it property instead of function or method)
# note: if your return from method is "str", python interpreter will display it instead of "NoneType"
# try using @property with the other function to know the difference.
# let's try after removing ()
person.legal_age
# Pass, you can enter the site

