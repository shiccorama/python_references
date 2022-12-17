# parent class :

class Food :
	# constructor :
	def __init__(self, food_name, food_price):
		# attributes :
		self.food_name = food_name
		self.food_price = food_price
	# methods :
	def eat(self):
		print(f"{self.food_name} and {self.food_price} from Food Parent")

# children classes :
# Don't forget to include the Parent class to the child class Fruits(Food)
class Fruits(Food):
	# consturctor :
	def __init__(self, food_name, food_price, is_fresh) :
		# attributes :
		# food_name will override the parent's attrib.
		# self.food_name = food_name
		# self.food_price = food_price
		# own attrib :
		self.is_fresh = is_fresh
		# now, we're going to inherit food_name, food_price from parent.
		super().__init__(food_name, food_price)
		# you can replace super() with class name, 
		# but it's preferrable to use super()
		# Food.__init__(self, food_price)

	# methods :
	# own methods :
	def check_fresh(self):
		if self.is_fresh == True :
			return (f"fresh")
		else :
			return (f"Bad")

	def display(self) :
		print(f"{self.food_name} are {self.check_fresh()} and price will be {self.food_price}")

# taking instances of Food and Fruits classes :

food_one = Food("Pizza", 120)
food_two = Fruits("Apples", 30, True)

food_one.eat()
print("_________")
food_two.eat()
food_two.display()

## _____ multi-level inheritance _____

class parent :
	def __init__(self):
		pass
	def one(self):
		print("def one from parent")

class child(parent):
	def __init__(self):
		pass
	def two(self):
		print("def two from child")
class grand_child(child):
	def __init__(self):
		pass
	def three(self):
		print("grand_child class can inherit from both parent and child as long as it can inherit from child")

parent_one = parent()
parent_one.one() # def one from parent
#parent_one.two() # parent cannot inherit from child or grand_child

child_one = child()
child_one.one() # def one from parent
child_one.two() # def two from child

grand_child_one = grand_child()
grand_child_one.one()  # def one from parent
grand_child_one.two()  # def two from child
grand_child_one.three() # grand_child class can inherit from both parent and child as long as it can inherit from child

## ______ Method Resolution Order (MRO) _____

# when you have a class that inherits from more than one class, the inherited class on the left will be executed first:

class A:
	def __init__(self):
		print("class A")

class B:
	def __init__(self):
		print("class B")

class C(B, A):
	# def __init__(self):
	# 	print("class C")
	pass

ob_c = C()  # class B - because you write it first
# it will print (class C) in case you un-has the constructor of class C
print(C.mro()) 
# output : [<class "__main__.C">, <class "__main__.B">, <class "__main__.A">, <class "object">]
# the order will be C >> B >> A