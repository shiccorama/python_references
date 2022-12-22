import sqlite3

def display_all():
    try:
        # make instance to connect to db:
        db = sqlite3.connect("/home/zorinsh/programming_lab/sqlite3/test_db_one.db")

        # printing successful message :
        print(f"successfully connected to db")

        # creating cursor to manipulate data :
        cr = db.cursor()

        # get all data from database by cursor execution :
        cr.execute(f"SELECT * FROM users")

        # store all fetched data into a variable :
        result = cr.fetchall()

        # print (result) as list of tuples :
        print(result)

        # print length of result:
        print(f"size of result :  {len(result)}")

        # loop over every item in this list :
        for row in result:
            print(f"userID => {row[0]}, userName => {row[1]}")
        
    except sqlite3.Error as err:
        # display error message :
        print(f"error happened", end=" ")
        print(f"{err}")

    finally:

        db.close()
        print(f"connection to database closed successfully")

display_all()