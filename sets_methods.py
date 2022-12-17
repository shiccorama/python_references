
# ____ sets in python _____

# sets are not indexed not mutable with curly braces 
mySet = {"hassan", 12, -1.5, ("ali", True)}
# sets can only have (strings, numbers, bool, and tuples only)
# sets CANNOT have (Lists or Dictionaries)
# print(mySet[1]) will not work because there is no indexing
# mySet[0] = "sara" will not work because sets are immutable
# sets are unique values means not repeated
# mySet = {"hassan","hassan","ali"} will not work


# ____ sets unqiue methods _______

# _____ union() or | ____

mySet1 = {1,2,3}
mySet2 = {4,5,6}
mySet3 = {7,8,9}

print(mySet1 | mySet2) # {1,2,3,4,5,6} , this will union two sets
print(mySet1.union(mySet2, mySet3)) # {1,2,3,4,5,6,7,8,9}

# _____ add() only one value ____

mySet1.add("hassan")
mySet1.add("ali")
print(mySet1)

# ____ copy() and clear() ____
print(mySet3.clear())  # none
mySet4 = mySet2.copy()  # shallow copy 
print(mySet4) # {4,5,6}


# ______ remove() vs discard() ______
mySet4.remove(5) # remove done by value # output = {4,6}
# mySet4.remove(11)  # will through an error
mySet4.discard(11) # will be ignored because there is no (11) value

# ______ remove random item by using pop() ______
mySet4.pop()  # remove random element because there in no index

# ______ update() vs union() ______
mySet4.update(mySet1)
print(mySet4)

# ____ difference() _______
a = {1,2,3,4}
b = {1,3,"hassan", "ali"}
c = a.difference(b)  # or (a-b)  
print(c)  # output = {2,4}


# ____ difference_update() or permenant mutation _______
g = {1,3,"hassan", "ali"}
h = {1,2,3,4,5}
g.difference_update(h)  # will update the original set itself
print(g)  # {"hassan", "ali"}

# ____ intersection() and intersection_update() _______

t = {1,2,3,4,"X"}
s = {"hassan", "X", 2}
d = t.intersection(s)  # or (t & s) 
print(d)  #{2, "X"}

s.intersection_update(d)
print(s) # permenant mutation => output = {2, "X"}

# ____ symmetric_difference() or (x ^ y) _______

e = {1, 2, 3, "ali", "sara"}
f = {1, "ali", 7, 8, 3}
j = e.symmetric_difference(f) # or (e ^ f) => different emelents
print(j)  # {2,7,8, "sara"}

# ____ symmetric_difference_update() _______
e.symmetric_difference_update(j) # done with mutation 
# output = {1,3,"ali",7,8}

# ___ issuperset()  && issubset()_____
t = {1,2,3,4,"X"}
l = {1,2}
print(t.issuperset(l)) # True, because all elements of l is found in t
# note: is(t) a superset of (l) not the opposite
print(l.issubset(t)) # True, becasue l is a subset of t

# ___ isdisjoint() _____
print(t.isdisjoint(l))  # False, because there are common items between them
o = {"ahmed", "ali"}
print(o.isdisjoint(l))  # True, because there are no common.