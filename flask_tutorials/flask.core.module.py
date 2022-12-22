# full tutorials on : https://python-web.teclado.com/section09/lectures/06_custom_css_jinja2/
# install flask by pip:
# pip install flask
# import from flash:

from flask import Flask as fl, render_template

my_flask_app = fl(__name__)

my_skills = [("html", "70"), ("css", "80"), ("javascript", "60"), ("php", "30")]

@my_flask_app.route("/")
def home():
    return render_template("home.html",page_title="Home Page")

@my_flask_app.route("/about")
def about():
    return render_template("about.html",page_title="About Us")

@my_flask_app.route("/addSkill")
def add_skill():
    # another way to make separate css file for each view is to pass props to the template
    # as the prop= customCSS
    return render_template("addSkill.html", page_title="Add Skill", 
                                            customCSS="addSkill",
                                            page_head="Show Skills",
                                            page_description="this page will show all the skills mentioned.",
                                            skills_list=my_skills)

if __name__ == "__main__":
    my_flask_app.run(debug=True,port=9000)