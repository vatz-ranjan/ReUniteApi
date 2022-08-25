import mongoengine

class PoliceStationDetails(mongoengine.Document):
    pid = mongoengine.StringField(required=True)
    shoName = mongoengine.StringField(required=True)
    shoNumber = mongoengine.IntField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'PoliceStationDetails'
    }

class PoliceLogin(mongoengine.Document):
    pid = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'PoliceLogin'
    }

class PoliceStationAddress(mongoengine.Document):
    pid = mongoengine.StringField(required=True)
    street = mongoengine.StringField(required=True)
    city = mongoengine.StringField(required=True)
    state = mongoengine.StringField(required=True)
    country = mongoengine.StringField(default='INDIA')
    zip_code = mongoengine.IntField(required=True)
    zone = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'PoliceStationAddress'
    }