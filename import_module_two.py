import module_two

# if you run module two, every thing in module one will run 
# except :
# (if this runs, it means we are running module one directly)
# because you're calling module one from another module, so you're NOT
# calling it directly from its place.

# if you try to print(__name__) from here, it will output (__main__)
# because we're in the same module
print(__name__)


# in module two, line 11 will give error because print(__name__) is NOT
# running from the same module
module_two.end_of_module()