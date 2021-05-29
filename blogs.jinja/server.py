from flask import Flask,render_template
import random
from datetime import date
toda = date.today()
current_year = toda.year
import requests


app = Flask(__name__)



@app.route('/')
def home():

    return render_template('index.html',year = current_year)



@app.route("/guess/<name>")
def guess(name):
    Name = name
    parameter = {
        'name': Name

    }
    response = requests.get(url='https://api.agify.io', params=parameter)
    response_age = requests.get(url='https://api.genderize.io',params=parameter)

    response.raise_for_status()
    data = response.json()
    age = data['age']
    gender = response_age.json()['gender']

    return render_template('index.html',naam = Name,umar=age,ling=gender,year = current_year)



@app.route("/blogs")
def blog():
    response = requests.get("https://api.npoint.io/0fd703c66228dcbd31f5")
    list_of_blogs = response.json()["blogs"]
    return render_template("blogs.html",list_of_blogs=list_of_blogs)











if __name__=="__main__":
    app.run(debug=True)