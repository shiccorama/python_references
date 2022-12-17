class CamelCaseName :
	# initialize the constructor
	def __init__(self, *Args, **kwargs):
		print(f"new object has been created")

# make new object from constructor method.
# we don't need to make new() method of the class.

object_one = CamelCaseName()
object_two = CamelCaseName()

object_one  # new object has been created
object_two  # new object has been created

# to know which class this object belongs to :
print(object_two.__class__) # < class "__main__.CamelCaseName >"

class AssignParams:
	def __init__(self, param1, param2):
		self.first_name = param1
		self.last_name = param2

# "self" represents the instance or the object itself, so we have
# to assign the parameters to "self" before using it to instantiate objects

user_one = AssignParams("hassan", "ali")
user_two = AssignParams("sara", "mohsen")

print(user_one.first_name, user_two.last_name) # hassan mohsen
print(dir(AssignParams))  # outputs all attributes and methods inside the class
print(dir(user_two)) # outputs all attrib + methods of this obejct
# object's attributes include first_name and last_name

##### ___________________ class methods and attributes _______________

# let's make new class with init method and another methods :

class BMIcalculation :
	# class attributes can be accessed by (classname.attrib)
	bmi = 1
	weight_result = 1
	height_result = 1

	# class method and static class method used without instances,
	# note: we have to declare it by using @classmethod & @static method before it
	# note: we have to pass class parameters to class method it by using (cls)

	@classmethod
	def class_method(cls):
		print(f"this is static class method used without instances")

	# now, let's take a look on static method:

	@staticmethod
	def static_method():
		print(f"this is static method which can be displayed without any parameters or arguments")

	# constructor functin __init__ with instance attributes :
	def __init__(self, height, weight, age, gender):
		self.height = height
		self.weight = weight
		self.age = age
		self.gender = gender
	# instance/object function/method :
	def convert_height(self):
		if self.height >= 100 :
			height_result = self.height
			print(f"@@{height_result}")
			return height_result
		else :
			height_result = self.height*2.54
			print(f"@@{height_result}")
			return height_result
	# instance/object function/method :
	def convert_weight(self):
		if self.weight <= 150 :
			weight_result = self.weight
			print(f"$${weight_result}")
			return weight_result
		else :
			weight_result = self.weight*0.454
			print(f"$${weight_result}")
			return weight_result

	# instance/object function/method :
	def is_obese(self):
		if BMIcalculation.bmi <= 35 :
			return (f"Normal")
		else:
			return (f"Obese")

	# instance/object function/method :
	def get_all_info(self):
		return (f"According to your age which is {self.age} and your gender which is {self.gender}, your height in cm is {self.convert_height()} and your weight in kg is {self.convert_weight()} + hello {BMIcalculation.bmi} + bye {self.is_obese()}")

# taking instances of the class and add attributes :
Hassan = BMIcalculation(180, 125, 43, "male")
Adel = BMIcalculation(70, 200, 22, "male")
Sara = BMIcalculation(88, 250, 65, "female")

# display the result of each instance :
print(Hassan.get_all_info())
print("#" * 20)
print(Adel.get_all_info())
print("#" * 20)
print(Sara.get_all_info())
print("#" * 20)
# display output of class_method
print(BMIcalculation.class_method())

# you have two methods to use instance's methods:
print(Sara.convert_weight())

# or you can use class name followed by instance method and call instance inside

print(BMIcalculation.convert_weight(Sara))

# let's try to output the static method :
print(BMIcalculation.static_method())


# ___ dunder or magic built-in methods ____
# __init__ , __str__, __len__, __class__, .....

class dunder_classes:
	def __init__(self):
		self.group = ["sara", "ahmed", "ali", "hassan"]

	def __str__(self):
		return (f"here you can write full description about your objects/instances")

	def __len__(self):
		return len(self.group)

employees = dunder_classes()
print(employees.group) #  ["sara", "ahmed", "ali", "hassan"]

for employee in employees.group:
	print(employee) # sara ahmed ali hassan 

print(len(employees.group))  # 4

# by using __len__, you can get length directly without (.group)
print(len(employees))  # 4

print(employees) # here you can write full description about ....

employees.group.append("maher")
employees.group.append("mostafa")

print(len(employees)) # 6





