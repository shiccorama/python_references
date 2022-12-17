# Dictionary is like Json 
# Dict cant hold list in its keys
# keys are immutable in dict.
# you can use tuples inside dict as either key or value
# you can use lists as value only
# keys in dict are unique, for example "name" can't be used more than once
# dict is not ordered, you can only access it by key 

user = {
	"name" : "Hassan",
	"age" : 33,
	"profession" : "Doctor",
	"hobbies" : ("reading","swimming","drawing"),
	(1,2,3) : "number of children"
}

print(user["age"])  # 33
print(user.get("age"))  # 33
print(user.keys())  # all keys
print(user.values())  # all values

# _________ Dictionary methods _______

# user.clear()
# user.update({"country" : "Russia"})
# user["gender"] = "male"
# newUser = user.copy()
# setdefault()

a = {"name": "sara"}
print(a.setdefault("name", "lara"))  # sara, because name is already a key inside
print(a.setdefault("age", 33)) # here, it will add age to keys because it's not found by default
# none == null in other programming languages
print(a.setdefault("hobbies")) # added to dict with none value
print(a) # {"name": "sara", "age": 33, "hobbies": None}

# popitem() will return the last item in the dict
print(a.popitem())  # will return tuple ("hobbies": None)
all_a_items = a.items()  # will store all items of {a} dict.
# if we add new item to {a}, it will consequently added to all_a_items
a["gender"] = "female"
print(all_a_items) # dict_items([("name","sara"),("age",33),("gender": "female")])
# you can make a new dict from tuples or lists by using fromkeys()

myList = [1,2,3]
myTuple = (4,5,6)
mySet = {7,8,9}

c = dict.fromkeys(myList,myTuple)
print(c)  # {1: (4,5,6), 2: (4,5,6), 3: (4,5,6)}
d = dict.fromkeys(myList,mySet)
print(d)  # {1: {7,8,9}, 2: {7,8,9}, 3: {7,8,9}}
e = dict.fromkeys(myTuple,myList)
print(e)  # {4: [1,2,3], 5: [1,2,3], 6: [1,2,3]}
f = dict.fromkeys(mySet,myTuple)
print(f) # {8: (4,5,6), 9: (4,5,6), 7: (4,5,6)}

## note : falsy values in python are (0, False, None, and any empty values)

print(bool(""))  # False

## not operator in python is equal to !
age = 30
print(not age > 40)  # True
print(not age > 20)  # False

####### type conversion #######
# you can use tuple() to convert List or Set to tuple
# but if you use tuple() with dict, you'll get only the keys

g = "sara"
print(tuple(g))  # ("s","a","r","a")

h = {"one" : 1, "two": 2}
print(tuple(h)) #  ("one", "two")

## same thing can be made by list() >>>>
## same thing can be made by set() >>>
## but keep in mind that set is always random in all cases
## you cannot make dict out of str,set,list,tuple