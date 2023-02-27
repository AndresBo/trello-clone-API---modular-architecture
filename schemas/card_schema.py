from main import ma
from marshmallow import fields

#create the Card Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class CardSchema(ma.Schema):
    class Meta:
        ordered = True
        # Fields to expose
        fields = ("id", "title", "description", "date", "status", "priority", "user")
    user = fields.Nested("UserSchema", only=("email",))

#single card schema, when one card needs to be retrieved
card_schema = CardSchema()
#multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)
