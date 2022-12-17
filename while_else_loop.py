## while loop instead of for loop:

a = 0
while a < 9 :  # condition is True
	print(a)
	a += 1
else:        # will be executed when condition is False
	print("a < 9")
	
	
while False
	print("this will not print because condition is already False")


### _______ for item in items loop _____

myList = [1,2,3,4,5]

for item in myList:
	print(item)
	if item % 2 == 0
		print(f"this {item} is even")


#### _______ loop in dict _______

mySkills = {
	"html" : "80%",
	"css" : "60%",
	"js" : "70%",
	"python" : "50%",
}

for skill in mySkills :
	print(f"to print the keys only use this {skill}")
	print(f"to print the values only use this {mySkills[skill]}")
	print(f"to print both Key:Value >> {skill}:{mySkills[skill]}")

### _____ nested loop ______

myUsers = {
	"hassan": {
		"html" : "80%",
		"css" : "60%",
		"js" : "70%",
		"python" : "50%",
	},
	"mohsen" : {
		"html" : "80%",
		"css" : "60%",
		"js" : "70%",
		"python" : "50%",
		},
	"shady" : {
		"html" : "80%",
		"css" : "60%",
		"js" : "70%",
		"python" : "50%",
	}
}


for user in myUsers :
		print(f"{myUsers[user]}")
		for skill in myUsers[user]:
			print(f"{myUsers[user][skill]}")


#### ______ advanced loop on Dict _______

print(f"{myUsers.items()}")

for key, value in myUsers.items() :
	print(f"{key} ==> {value}")
	# print(f"{key.items()}")
	for k, v in value.items() :
		print(f"{k} _____ {v}")

#### _____ unpack arguments with (*) _________

num = [1,2,3,4,5,6]
# printing this list will output [1,2,3,4,5,6]
# but what if I want to print each item separately without [ ]
# like this : 1 2 3 4 5 6  >>>> ??
print(num)  # [1,2,3,4,5,6]
print(*num)  # 1 2 3 4 5 6
 # note : default parameter must be last parameter sayHi(name,age,country="USA")

 ## difference between *Args and **kArgs :

 def show_skills(*Args):
 	print(type(Args))
 	for skill in Args:
 		print(f"{skill}")

 show_skills("html", "css", "js")
 # <class "tuple"> and  html, css, js

  def show_skills(**KArgs):
 	print(type(KArgs))
 	for key,value in KArgs.items():
 		print(f"{key} ==> {value}")

 show_skills(html="80%", css="70%", js="50%")
 # <class "dict">
 # html ==> 80%
 # css ==> 70%
 # js ==> 50%

 myDict = {
 	"html" : 33,
 	"css" : 44,
 	"js" : 55
 }

 show_skills(**myDict)  ## you have to recall the dict with ** 