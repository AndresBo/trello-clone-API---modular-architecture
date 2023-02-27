from main import ma
from marshmallow.validate import Length
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ['id', 'email', 'password', 'admin', 'cards']
        load_only = ['password', 'admin']
    #set the password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6))
    cards = fields.List(fields.Nested("CardSchema", exclude=("user",)))

user_schema = UserSchema()
users_schema = UserSchema(many=True)
