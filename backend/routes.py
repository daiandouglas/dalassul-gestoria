from flask import render_template, url_for, flash, redirect
from app import app, db
from models import User, Project, Task

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

# ...existing code...
