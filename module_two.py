# module two

print(f"this is module two")

if __name__ == "__main__" :
    print(f"if this runs, it means we are running module two directly")
else :
    print(f"this means we're not running module two directly")


print(__name__)
# output (__main__)

def end_of_module():
    print(f"module two finished")