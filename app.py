from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userprofile.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

@app.before_first_request
def create_table():
    db.create_all()

class Users(db.Model):
    user_name = db.Column(db.String(30), unique=False, nullable=False, primary_key=False)
    user_email = db.Column(db.String(30), unique=True, nullable=False, primary_key=False)
    user_password = db.Column(db.String(), primary_key=True, nullable=False, unique=True)
    user_age = db.Column(db.String(30), unique=False, nullable=False, primary_key=False)
    user_bio = db.Column(db.String(30), unique=False, nullable=False, primary_key=False)
    user_job = db.Column(db.String(30), unique=False, nullable=False, primary_key=False)
    user_interest = db.Column(db.String(30), unique=False, nullable=False, primary_key=False)



    def __repr__(self):
        return f"User('{self.user_name}', '{self.user_email}', '{self.user_password}',{self.user_age})"
        # return "<Title: {}>".format(self.title){self.username}', '{self.email}', '{self.image_file}

@app.route("/", methods=["GET","POST"])
def home():
    if request.form:
        name_from_form = request.form.get('user_name')
        email_from_form = request.form.get('user_email')
        password_from_form = request.form.get('user_password')
        age_from_form = request.form.get('user_age')
        bio_from_form = request.form.get('user_bio')
        job_from_form = request.form.get('user_job')
        interest_from_form = request.form.get('user_interest')

        user = Users(user_name=name_from_form, user_email=email_from_form,
               user_password=password_from_form, user_age=age_from_form,
               user_bio=bio_from_form, user_job=job_from_form, user_interest=interest_from_form,)
        db.session.add(user)
        db.session.commit()
    userprofile = Users.query.all()
    return render_template('index.html', userprofile = userprofile)
