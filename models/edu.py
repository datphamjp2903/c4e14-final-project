from mongoengine import *

class Edu(Document):
    name = StringField()
    district = StringField()
    city = StringField()
    fee = IntField()
    phone = StringField()
    rate = IntField()
    courses = ListField(StringField())

    
