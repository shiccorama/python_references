# timeit is a module to measure your code performance
# it runs by 1M time and gives you minimum time output
# timeit(statement, setup, timer, counter)
# timeit(pass, pass, default, 1.000.000) default values

# statement: the code that you want to measure its timing
# setup: any setup you want to perform before execution like importing a module for example
# timer: timer value in milli-seconds
# counter: how many times the code will execute

import timeit
# you can remove import random as long as you use it in setup
import random

# print(dir(timeit))

# test small code :
print(timeit.timeit("'repeated word' * 1000"))

# another test :
print(timeit.timeit("name = 'hassan' ; name * 1000"))

# using import random
print(timeit.timeit(stmt="random.randint(0,50)", setup="import random"))

# using repeat :
print(timeit.repeat(stmt="random.randint(0,50)", setup="import random", repeat=4))
# repeat will repeat the whole process 4 times, so it will output 4 results
