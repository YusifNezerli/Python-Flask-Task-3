from extensions import db
from app import app

class Producer(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(100), nullable = True)

    def __repr__(self):
        return {self.name}
    
    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

class Movie(db.Model):
    id=db.Column(db.Integer, primary_key =True)
    name=db.Column(db.String(50), nullable= True)
    year=db.Column(db.Integer, nullable=True)
    imdb=db.Column(db.Float, nullable=False)
    producer_id = db.Column(db.Integer, db.ForeignKey('producer.id'), nullable=False)
    producer = db.relationship('Producer', backref=db.backref('movies', lazy=True))
    status=db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.name  
    
    def __init__(self, name, year, imdb, producer_id, status):
        self.name = name
        self.year = year
        self.imdb = imdb
        self.producer_id = producer_id
        self.status = status
        

    def save(self):
        db.session.add(self)
        db.session.commit()



        






