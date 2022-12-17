# https://pythex.org  >>> to check your regular expressions.
# https://www.debuggex.com/cheatsheet/regex/python  >> cheat sheet
# https://regex101.com

# match emails regex :
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# [A-z0-9\.]+@[a-Z0-9]+\.(com|org\net|info)

# _______________use regex with python files__________

# first import re or regex module:
import re

# search_pattern = re.search(regex, string)

search_regex = re.search(r"[A-Z]{2}", "OOsamaEElzero")

print(search_regex)  # <re.Match object; span=(0,2), match="OO">
print(search_regex.span()) # (0,2)
print(search_regex.string) # OOsamaEElzero
print(search_regex.group()) # OO

search_regex = re.search(r"[0-9]{2}", "OOsamaEElzero")

print(search_regex)  # None , because there are no numbers

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]+", "zeroPlus.note@link.net")

if(is_email):
    print(is_email)
else:
    print(f"it's not a valid email")


# findall() is a function that returns an empty list if regex not found
# or list of regex if match happens.
# findall( regex, string)

get_input = input(f"please enter your email")

my_email_list = []

findall_list = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]+", get_input)

if(findall_list != []):
    my_email_list.append(get_input)
    print(f"email is added to my list")
else:
    print(f"invalid email")

for email in my_email_list:
    print(email)

# re.split(regex, string, max-step)
# re.split return a list of cutted strings
# split will cut the string at regex with max steps you give

str_one = "here we are,bro but listen to me"
apply_split1 = re.split(r"\s", str_one, 2)
print(apply_split1)  # ["here", "we", "are,bro but listen to me"]
# max 2 spaces applied

str_two = "How-to_Write_A_VERy-good-article"
apply_split2 = re.split(r"-|_", str_two)
print(apply_split2)

# applying enumerate with loop in the above example

for count, word in enumerate(apply_split2, start=1):
    print(f"{count} => {word.lower()}")

# re.sub(regex, replace, string, replace count)
# re.sub used to replace regex match with whatever string you want.
# let's apply on str_two, to replace all (-|_) with "$"

apply_sub = re.sub(r"-|_", "$", str_two, 4)
# note: we chose to change only 4 characters of 6
print(apply_sub) # How$to$Write$A$VERy-good-article

# group and groups in regex search :

url = "https://www.elzero.org:8080/category.php?article=105?name=how-do-you-do"

match_regex = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", url)

print(match_regex.groups())
# you need to check first if match_regex is not None
# groups will print ("https", "www", "elzero", "org", "8080", "category.php?article=105?name=how-do-you-do" )
# you can loop over groups to get each word separately.

print(match_regex.group(1)) # "https"
print(match_regex.group(5)) # "8080"

# url = protocol + sub domain + domain name + top level domain + port + query string

# how to write flags ( like global, ignore case, dotall, ...)

name = "OSAMA"
flags = re.search(r"[a-z]", name, re.I) # ignore case