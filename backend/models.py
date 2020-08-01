from .app import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    pw = db.Column(db.Unicode)
    date_made = db.Column(db.DateTime)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()
        
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.Unicode, nullable=False)

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.date_joined = datetime.now()
        self.token = secrets.token_urlsafe(64)