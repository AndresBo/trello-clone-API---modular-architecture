from main import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    cards = db.relationship(
        "Card",
        backref="user",
        cascade="all, delete"
    )
    comments = db.relatioship(
        "Comment",
        backref="user",
        cascade="all,delete"
    )
