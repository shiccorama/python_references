myTyple1 = ("html", "css", "js")

myDict1 = {
	"Go" : "20%",
	"python" : "70%",
	"nodejs" : "40%"
}


def show_skills(name, *Args, **KArgs):
	print(f"My name is {name}, and my skills are :")

	for item in Args :
		print(f"{item}")

	for k, v in KArgs.items():
		print(f"{k} ==> {v}")


show_skills("hassan", myTyple1, myDict1)
# output :
# My name is hassan, and my skills are :
#("html", "css", "js")
#{"Go": "20%", "python" : "70%", "nodejs" : "40%"}


show_skills("hassan", *myTyple1, **myDict1)
# output :
# My name is hassan, and my skills are :
# html
# css
# js
# Go ==> 20%
# python ==> 70%
# nodejs ==> 40%