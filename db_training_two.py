# import sqlite3 database module :
import sqlite3

# taking instance to deal with saved database :
db = sqlite3.connect("/home/zorinsh/programming_lab/sqlite3/test_db_one.db")

# apply cursor to execute on db :

cr = db.cursor()

uid = 5

# let's make a method that commit and close connection to database:

def commit_close_db():
    db.commit()
    db.close()
    print(f"connection closed successfully")

# app message to user :
input_message = """
choose from below options:
"c" => create skill
"r" => retrieve one skill
"u" => update skill
"d" => delete skill
"s" => show skills
your option is :
"""

# display input field :
user_input = input(input_message).strip().lower()

# let's make list from given options :
options = ["c", "r", "u", "d", "s", "q"]

# let's make CRUDS operations first and hen check and choose suitable operation :

def create_skill():

    skill_name = input(f"Add skill name : ").strip().lower()
    skill_progress = input(f"Add skill progress: ").strip()

    # let's check if this skill is already in db or not :

    cr.execute(f"SELECT name FROM skills WHERE name = '{skill_name}' AND user_id  = '{uid}'")
    result = cr.fetchone()

    if result == None :
        # means there is no skill with this name in db
            cr.execute(f"INSERT INTO skills(name, progress, user_id) VALUES('{skill_name}', '{skill_progress}', '{uid}')")
            print(f"skill created")
            commit_close_db()
    else:
        # means it is already in db, do you want to update it
        is_update = input(f"skill exists, do you want to update it? choose letter (y or n): ").strip().lower()
        if is_update == "y":
            update_skill()
        else:
            print(f"program terminated")

    

def retrieve_skill():
    skill_name = input(f"select skill name : ").strip().lower()
    cr.execute(f"SELECT name, progress FROM skills WHERE name = '{skill_name}' AND user_id  = '{uid}'")
    print(cr.fetchone())
    print(f"skill retrieved")
    commit_close_db()

def update_skill():
    skill_name = input(f"update skill name : ").strip().lower()
    skill_progress = input(f"update skill progress: ").strip()
    cr.execute(f"UPDATE skills SET progress = '{skill_progress}' WHERE name = '{skill_name}' AND user_id = '{uid}'")
    print(f"skill updated")
    commit_close_db()

def delete_skill():
    skill_name = input(f"delete skill name : ").strip().lower()
    cr.execute(f"DELETE FROM skills WHERE name = '{skill_name}' AND user_id = '{uid}'")
    print(f"skill deleted")
    commit_close_db()

def show_skills():
    print(f"skills are shown below")
    cr.execute(f"SELECT * FROM skills WHERE user_id = '{uid}'")
    result = cr.fetchall()
    print(f"you have {len(result)} skills")
    if len(result) <= 0 :
        print(f"Do you want to add any?", end = " ")
        is_create = input(f"choose letter (y or n): ").strip().lower()
        if is_create == "y":
            create_skill()
        else:
            print(f"program terminated")
    else:
        for row in result:
            print(f"skill name => {row[0]}, skill progress => {row[1]}")
        commit_close_db()

# check user response :
if user_input in options:
    print(f"you chose \"{user_input}\" ")

    if user_input == "c":
        create_skill()
    elif user_input == "r":
        retrieve_skill()
    elif user_input == "u":
        update_skill()
    elif user_input == "d":
        delete_skill()
    elif user_input == "s":
        show_skills()
    else:
        print(f"app's closed")

else:
    print(f"please select suitable letter from above")
