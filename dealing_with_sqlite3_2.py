# import sqlite3 database module :
import sqlite3

# taking instance to deal with saved database :
db = sqlite3.connect("/home/zorinsh/programming_lab/sqlite3/test_db_one.db")

# apply cursor to execute on db :

cr = db.cursor()

# let's print all data table :

cr.execute("SELECT * FROM users")

print(cr.fetchall())

# let's update some fields in db:

cr.execute("UPDATE users SET user_name = 'tarek' WHERE user_id = 3")

# let's insert into user table :

cr.execute("INSERT INTO users(user_id, user_name) VALUES(8, 'dalia')")

# let's delete a user from table :

cr.execute("DELETE FROM users WHERE user_id = 4")

# final update :

cr.execute("UPDATE users SET user_id = 9 AND user_name = 'mona' WHERE user_id = 8")

# final delete :

cr.execute("DELETE FROM users WHERE user_id = 0")

# now, let's see the results after update, add, and delete records :

cr.execute("SELECT * FROM users")

print(cr.fetchall())

# [(1, 'ahmed'), (2, 'ali'), (3, 'tarek'), (5, 'sara'), (6, 'lara'), (7, 'enas')]

# don't forget to commit your db:

db.commit()

# don't forget to close the connection :

db.close()