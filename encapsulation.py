# Encapsulation restricts access and modification of class attributes and methods
# Encapsulation has three divisions (public, protected, private)
# public  : allow access and modificatin from inside and outside the class
# protected : allow access from within the class and sub-classes or inherted classes
#          : attributes and methods prefixed with underscore for separation 
# private : access granted from the class itself only
#		  : attributes and methods cannot be modified
#		  : attributes and methods prefixed with double underscores

### ________________________________________ ###
# important rule: encapsulation is actually not wroking in python
# you can consider it as naming convention for the team work
# in other words, to mark the attribute as private or public
# but access granted for all (all elements considered PUBLIC )
### ________________________________________ ###

class Member:
    def __init__(self, public_attrib, protected_attrib, private_attrib,):
        self.public_attrib = public_attrib # public without underscore
        self._protected_attrib = protected_attrib # protected with one underscore
        self.__private_attrib = private_attrib # private with double underscore

        print(f"public = {self.public_attrib}, protected = {self._protected_attrib}, private = {self.__private_attrib}")
    def inside_class(self):
        print(f"I can access protected and private attributes because I am inside the same class, see! protected = {self._protected_attrib}, private = {self.__private_attrib}")

class Child(Member):
    def __init__(self):
        # super().__init__()
        print(f"child class")

# public:

var_one = Member("pub", "pro", "priv") # public = pub, protected = pro, private = priv
# you can modify values as you want:
var_one.public_attrib = "change one"
print(var_one.public_attrib) # change one
var_two = Child()  # child class
var_two.public_attrib = "change two"
print(var_two.public_attrib) # change two

# protected:

print(var_one._protected_attrib)  # pro
var_one._protected_attrib = "change three"
# protected attributes can be changed as you can see
print(var_one._protected_attrib)  # change three

# private:

print(var_one.__private_attrib)  # AttributeError (private attribute)
print(var_one.inside_class())
# output : I can access protected and private attributes because I am inside the same class, see! protected = change three, private = priv

# you can access it by using this way (even if it's private !!!)

print(var_one._Member__private_attrib)  # priv
var_one._Member__private_attrib = "change four"
print(var_one._Member__private_attrib)  # it is not working
