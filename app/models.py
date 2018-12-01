from app import db

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    email = db.Column(db.String(254), index=True, unique=True)

    def __repr__(self):
        return f'<User {self.name}>'