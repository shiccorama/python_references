# check list of exceptions at :
# https://docs.python.org/3/library/exceptional.html

# raise your own exception using keyword : raise 

x = -10

if x < 10:
    raise Exception(f"problem found, number's less than 10")

print(f"pass, and continue the program because number's bigger than 10")

# output : problem found, number's less than 10
# so, you can use this message to give you errors if your app goes out of track

# try + except + else + finally usage :

try:     # will test the code and validate it :
    your_age = int(input(f"please enter your age in numbers"))

    # suppose that person will enter their own age in words(thirty-three)

except:  # will raise the error message if the code didn't pass
    print(f"this is not a number, please enter a valid number")

else:   # if everything goes well, the program will continue
    print(f"your age passes the exception stage")

finally: # will be executed anyway in the end of the program 
    print(f"end of the program")

## you can use more than one exception :

try :
    #print(a)
    print(23/0)
except ZeroDivisionError :
    print(f"you cannot divide any number on zero")
except NameError :
    print(f"there is no variable named a")
except ValueError :
    print(f"cannot print int from string")
except :
    print(f"this will be general error not specific")

# as the error found, the message will be displayed


# example on how to open a file with its path:

the_file = None
count = 5

while count > 0 :
    try:
        open_file = input(f"please enter the path of your file:").strip()
        print(f"you have {count} left")
        the_file = open(open_file, "r")
        print(the_file.read())
        break
    except FileNotFoundError:
        print("you've entered wrong path, try again")
        count -= 1
    except :
        print(f"this is generic error")
    finally:
        if the_file is not None:
            the_file.close()
            print(f"file is closed successfully")
else:
    print(f"you're run out of trials")


def calc_sum(n1, n2): -> int
    print(n1 + n2)

# -> int (is a hint that this function accepts only integers)
# -> str
# -> bool
# -> float