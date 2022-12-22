# log types are ( debug, info, warning, error and critical)
# logs can be displayed on terminal or .log file

# first import logging module :
import logging

# second explore everything inside it :
# print(dir(logging))

# logging.basicConfig(filename="", filemode="", formatstring="", datefmt="")

logging.basicConfig(filename="firstLog.log", filemode="a", format="logger_name = %(name)s, time = %(asctime)s, level_name = %(levelname)s, message = %(message)s", datefmt="%d %B %Y, %H:%M:%S", level=logging.WARNING)

# debug message :
logging.debug("this is DEBUG message!") # this will not appear because system doesn't care about debug or info
logging.info("this is info message!") # same here , system doesn't care about info

logging.warning("this is warning message!")
logging.error("this is error message!")
logging.critical("this is critical message!")
# all the above 3 line will output this: ( of course with different names => warning, error and critical)
# logger_name = root, time = 20 December 2022, 13:28, level_name = CRITICAL, message = this is critical message!

my_first_logger = logging.getLogger("instead_of_root")
my_first_logger.error("this is my custom error message for my first logger")