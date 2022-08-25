import mongoengine

class DummyDetails(mongoengine.Document):
    oneOne = mongoengine.StringField()
    two = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'DummyDetails'
    }