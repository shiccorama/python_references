class Food :
	def __init__(self, private_attrib):
		self.__private_attrib = private_attrib

	def Recipe(self):
		return (f"this is {__private_attrib} recipe")


	## define getter and setter methods ##

	def getter(self):
		return self.__private_attrib

	def setter(self, new_attribute):
		self.__private_attrib = new_attribute
		

fruit = Food("mango") 
 # taking instance from Food class

fruit._Food__private_attrib = "banana" 
 # changing private attribute using _className__attribute method

print(fruit._Food__private_attrib)
 # changing done from "mango" to "banana"

print(fruit.getter())  # banana
fruit.setter("orange")
print(fruit.getter()) # setter