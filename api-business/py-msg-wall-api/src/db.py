from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    author = db.Column(db.String(32))
    created_date = db.Column(db.DateTime)
    last_update = db.Column(db.DateTime)
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)

    def create_and_save(self):
        self.created_date = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()
