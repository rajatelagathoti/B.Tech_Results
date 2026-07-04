import streamlit as st
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/submit", methods=["POST"])
def submit():
    print(request.form)

    name = request.form["name"]
    age = request.form["age"]
    phnumber = request.form["phnumber"]
    gender = request.form["gender"]
    college = request.form["college"]
    locality = request.form["locality"]

    print(name, age, phnumber, gender, college, locality)

    return "Data received successfully"

app.run(debug=True)
