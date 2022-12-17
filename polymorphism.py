# polymorphism is a group of functions that have the same name
# but have different input and different output according to their locations.

class A :
	def __init__(self):
		pass
	def must_be_implemented(self):
		print(f"By adding the next raise exception, all inherited classes will have to implement this function one way or another")
		print(f"implementation is optional as long as you didn't enforce the inherited classes to do so")
		raise NotImplementedError("All inherited classes must implement this method")

class B(A):
	def __init__(self):
		pass
	def must_be_implemented(self):
		print(f"I am a good class, I inherited from class A and implemented its method")

class C(B):
	def __init__(self):
		pass


object_c = C()
object_c.must_be_implemented()
# output (I am a good class, I inherited from class A and implemented its method)
# def must_be_implemented() is a polymorph function because it has
# two different shapes in class A & B
# if we 

class D(A):
	def __init__(self):
		pass
	def naughty_class(self):
		print(f"I inherited from class B, so I also inherited from class A, but I am not going to implement its method")
object_d = D()
object_d.must_be_implemented()
# output ( raise exception : All inherited classes must implement this method)

