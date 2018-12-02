from app import db

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    email = db.Column(db.String(254), index=True, unique=True)
    answers = db.relationship('Answer', backref='voter', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.name}>'

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    path = db.Column(db.String(20))
    language = db.Column(db.String(20))
    comment = db.Column(db.String(200))
    voter_id = db.Column(db.Integer, db.ForeignKey('voter.id'))

    def __repr__(self):
        return f'<Answer {self.age, self.gender, self.path, self.language}>'
