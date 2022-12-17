# zip() return a zip object contains all iterable objects
# zip() length in loop is equal to the shortest length of the iterables
# example

list_one = [1,2,3,4,5]
list_two = [6,7,8]

combined_lists = zip(list_one, list_two)
print(combined_lists)  # <zip object at 0x00234343778>

for item in combined_lists:
	print(item)  # (1,6) (2,7) (3,8)

# print does NOT output (,4) and (,5) because zip takes the shortest of them.

tuple_one = ("a", "b", "c")
dict_one = {
	"name" : "Hassan",
	"age" : 33,
	"profession" : "Doctor",
	"hobbies" : ("reading","swimming","drawing"),
	(1,2,3) : "number of children"
}

# for loop to join all of list, tuple and dict:
combined_iterables = zip(list_one, list_two, tuple_one, dict_one)

for a,b,c,d in combined_iterables:
	print(a)
	print(b)
	print(c)
	print(d)

# every iterator will loop over one iterable
# a for list_one, b for list_two, ....
# output
# 1 6 1 name, 2 7 b age, 3 8 c profession

# if you want the value of the dict, you need to unpack dict:

for a,b,c,d in zip(list_one, list_two, tuple_one, dict_one):
	print(a)
	print(b)
	print(c)
	print(d)
	print(dict_one[d])