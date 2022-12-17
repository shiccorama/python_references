
# _______ append method ____

myList = [1,2,3,4]
myList.append(5)  # note: append() takes only one argument at a time
print(myList) # [1,2,3,4,5]
myList.append([6,7,8]) # [1,2,3,4,5,[6,7,8]]
print(myList[5][1])   # 7


# _______ extend method ____

newList = ["a", "b", "c"]
myList.extend(newList)
print(myList)  # [1,2,3,4,5,[6,7,8],"a","b","c"]

# _______ remove method ____

myList.remove(5) # will delete the first encounter only
print(myList) # [1,2,3,4,5,[6,7,8],"a","b","c"]

# _______ sort method ____

newList = [1,2,100,120,-10,17,27]
newList.sort()  # [-10,1,2,17,27,100,120]
newList.sort(reverse=True)  # [120,100,27,17,2,1,-10]
# sort() can sort int only or characters only (a,b,c,...)

# _______ reverse method ____
# reverse() will reverse the arrangement without considering the values

newList = [2,5,3,"c","x","p"]
newList.reverse()
print(newList)  # ["p","x","c",3,5,2]

# _______ clear method ____

a = [1,2,3]
a.clear()  # []

# ______ copy method _____

a = [1,2,3]
b = a.copy()  # shallow copy (doesn't alter main list)
print(b) # considered separated list

# ______ count method _____

c = [1,2,3,4,4,3,3,5,5,7]
print(c.count(4))  # how many 4 in the list, output = 2

# ______ index method _____

print(c.index(4))  # index of value 4 = 3

# ______ insert method _____
# insert(index, value)
# insertion will be before the index you write

c.insert(5,17)
print(c)  # [1,2,3,4,4,17,3,3,5,5,7]

# ______ pop method _____
# pop(index)
# pop is not like javascript, pop returns the index you write

c = [1,2,3,4,4,17,3,3,5,5,7]
print(c.pop(5))   # 17

# ______ Tuple method _____
# Tuple can be written with () or without:
myTuple = (1,2,3)
myTyple1 = 1,2,3
# you can differentiate between variables and tuples by (,):
myVar = "Hassan"
myTuple2 = "Hassan",  # or ("Hassan",)
print(type(myVar))  # < class "str" >
print(type(myTuple2)) # < class "tuple" >

# ______ Tuple concatenation _____

w = (3,5,7)
u = (9,3)
y = w + u
print(y)  # (3,5,7,9,3)

# ____Tuple, List, String (repeat *)__

print(u * 3) # (9,3,9,3,9,3)
print(w * 2) # (3,5,7,3,5,7)

# ______ Tuple destruction _____

w = (3,5,7)
r, s, t = w # it means r=3, s=5, t=7
a, b = w # error, because (w) has 3 items, to escape item use (_)
a, _, b = w  # a=3, b=7





