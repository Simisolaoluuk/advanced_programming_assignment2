from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String(200), nullable=False)

    companies = db.relationship("Company", backref="status", lazy=True)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    number = db.Column(db.String(50))
    postcode = db.Column(db.String(20))

    status_id = db.Column(db.Integer, db.ForeignKey("status.id"), nullable=False)
