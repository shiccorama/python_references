def clean(str):
	if len(str) == 1:
		return str

	if str[0] == str[1]:
		return clean(str[1:])

	return str[0] + clean(str[1:])


print(clean("WWWoooorrrldd"))


### lambda function : Anonymous function

def say_hello(param) : return f"hello {param}"

anyVariable = lambda param : f"hello {param}"

print(say_hello("hassan"))  # hello hassan
print(anyVariable("ali"))   # hello ali

print(say_hello.__name__)  # say_hello as the name of function
print(anyVariable.__name__) ## <lambda>  --- anonymous function
print(type(anyVariable))  ##  <class "function">