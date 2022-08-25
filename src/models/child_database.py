import mongoengine

class ChildInfo(mongoengine.Document):
    firNo = mongoengine.StringField(required=True)
    pId = mongoengine.StringField(required=True)
    firstName = mongoengine.StringField(required=True)
    middleName = mongoengine.StringField()
    lastName = mongoengine.StringField()
    firNo = mongoengine.StringField(required=True)
    firDate = mongoengine.StringField(required=True)
    gender = mongoengine.StringField(required=True)
    dob = mongoengine.StringField()
    age = mongoengine.IntField()
    dateOfMissing = mongoengine.StringField()
    placeOfMissing = mongoengine.StringField()
    height = mongoengine.StringField()
    weight = mongoengine.StringField()
    complextion = mongoengine.StringField()
    built = mongoengine.StringField()
    bloodGroup = mongoengine.StringField() 
    hairColour = mongoengine.StringField()
    imageURL = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'ChildInfo'
    }

class ChildInformantInfo(mongoengine.Document):
    firNo = mongoengine.StringField(required=True)
    informantName = mongoengine.StringField()
    informantRelation = mongoengine.StringField()
    informantEmailId = mongoengine.StringField()
    informantPhoneNumber = mongoengine.StringField()
    informantAddress = mongoengine.StringField()

    meta = {
        'db_alias': 'core',
        'collection': 'ChildInformantInfo'
    }

class ChildFaceEncoding(mongoengine.Document):
    firNo = mongoengine.StringField(required=True)
    face_encoding = mongoengine.BinaryField()
    isFound = mongoengine.BooleanField(default=False)

    meta = {
        'db_alias': 'core',
        'collection': 'ChildFaceEncoding'
    }