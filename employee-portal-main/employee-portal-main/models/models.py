from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 


class Employee(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50)) 
    gender = db.Column(db.String(10)) 
    address = db.Column(db.String(255)) 
    phone = db.Column(db.Integer) 
    alary = db.Column(db.Integer) 
    epartment = db.Column(db.String(50)) 