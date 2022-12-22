# import sqlite3 module :
import sqlite3

# create new Database and connect to it :

db = sqlite3.connect("/home/zorinsh/programming_lab/sqlite3/test_db_one.db")

# create tables and fields :

# db.execute("CREATE TABLE skills (name text, progress integer, user_id integer)")

# you can create database by the above command, but when you're going to run the
# file again, python interperter will give you an error because database already exists
# so, you need to add (if not exists) to the above command to avoid this error

# db.execute("CREATE TABLE if not exists skills (name text, progress integer, user_id integer)")

# setting up the cursor for db :

cursor = db.cursor()

cursor.execute("CREATE TABLE if not exists users(user_id integer, user_name text)")
cursor.execute("CREATE TABLE if not exists skills (name text, progress integer, user_id integer)")

# inserting data into database by using insert into :

# cursor.execute("INSERT INTO users(user_id, user_name) Values0(1, 'ahmed')")

# now, let's make a list of users to insert it once in database :

users_list = ["ahmed", "ali", "hassan", "kareem", "sara", "lara", "enas"]

# to insert all users into db, we execute insertion command by using for in loop :

# for key, user in enumerate(users_list):
#     cursor.execute(f"INSERT INTO users(user_id, user_name) VALUES({key+1}, '{user}')")
# note, we use {key+1} because key starts with zero
# note, we use '{user}' in quote, because users should store in db as strings
# without quotation, the error displayed is "no such column : ahmed" because it sees it as column head not value.
# we use single quote inside double qoute to pass the '{user}'

# selecting data and show it using fetchone(), fetchmany(integer), fetchall() :

# cursor.execute(f"SELECT user_name FROM users") # this will bring only one field : user_name as a tuple ("ahmed",)
# cursor.execute(f"SELECT user_id, user_name FROM users") # this will bring list of tuples [(user_id, user_name)] => [(1, "Ahmed"),]
cursor.execute(f"SELECT * FROM users")  # this will select all data from table users

print(cursor.fetchone()) # [(1, "Ahmed"),]
# every time you print cursor.fetchone() will bring you one record and finally it will return None when all records are finished.

print(cursor.fetchmany(3))  # [(2, 'ali'), (3, 'hassan'), (4, 'kareem')]
# fetchmany(integer) will bring you exactly how many fields you'd like to display

print(cursor.fetchall()) # [(5, 'sara'), (6, 'lara'), (7, 'enas')]
# this will bring you the rest, but if you use it first, it will bring you the whole 7 fields


# before closing connection , you have to save it by (commit) command :
# remember, you're commiting the db, not the cursor itself :
db.commit()

# now, let's try to close the connection :

db.close()