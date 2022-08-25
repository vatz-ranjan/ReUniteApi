import mongoengine

class CitizenDetails(mongoengine.Document):
    emailId = mongoengine.EmailField(required=True)
    firstName = mongoengine.StringField(required=True)
    middleName = mongoengine.StringField()
    lastName = mongoengine.StringField()
    phoneNumber = mongoengine.LongField(required=True)
    governmentId = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'CitizenDetails'
    }

class CitizenLogin(mongoengine.Document):
    emailId = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'CitizenLogin'
    }

class CitizenAddress(mongoengine.Document):
    emailId = mongoengine.StringField(required=True)
    street = mongoengine.StringField(required=True)
    city = mongoengine.StringField(required=True)
    state = mongoengine.StringField(required=True)
    country = mongoengine.StringField(default='INDIA')
    zip_code = mongoengine.IntField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'CitizenAddress'
    }
