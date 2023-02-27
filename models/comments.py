from main import db


class Comment(db.Model):
    # define the table name for the db
    __tablename__="comments"
    
    id = db.Column(db.Integer, primary_key=True)
    # add the rest of the attributes:
    message = db.Column(db.String())
    # two-foreign keys:
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey("cards.id"), nullable=False)
