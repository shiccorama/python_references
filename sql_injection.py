import sqlite3

db = sqlite3.connect("/home/zorinsh/programming_lab/sqlite3/test_db_one.db")

cr = db.cursor()

# YOU CAN STORE YOUR DATA IN A TUPLE AND INJECT IT INTO SQL COMMANDS
# TO AVOID INSERTION FROM OUTSIDE LIKE THIS :

# insertion = (skill name, skill progress, user id)
new_insertion = ("css", "68", 1)

# FIRST, YOU CAN REMOVE (NAME, PROGRESS, USER ID) FROM QUERY
# SECOND, WE HASH THE INPUTS OF VALUES BY (?, ?, ?)
# THIRD, WE ADD COMMA AFTER VALUES AND INSERT OUR INSERTION VARIABLE

cr.execute("INSERT INTO skills VALUES(?, ?, ?)", new_insertion)

# YOU CAN DIRECTLY INSERT VALUES LIKE THIS , WITHOUT ASSIGNMENT
# cr.execute("INSERT INTO skills VALUES(?, ?, ?)", ("css", "68", 1))

result = cr.fetchall()

for row in result:
    print(f"{row[0] --- row[1]}")

# commit/save your db and close :
db.commit()
db.close()
