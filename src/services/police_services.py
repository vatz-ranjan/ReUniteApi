from MissingChild.src.face_detection import face as Face
from src.models.police_database import PoliceLogin
from src.models.police_database import PoliceStationDetails
from src.models.police_database import PoliceStationAddress
from src.models.child_database import ChildInfo
from src.models.child_database import ChildInformantInfo
from src.models.child_database import ChildFaceEncoding

def create_account(registration_info):
    pId = registration_info.get('pId', None)
    password = registration_info.get('password', None)
    shoName = registration_info.get('shoName', None)
    shoNumber = registration_info.get('shoNumber', None)
    street = registration_info.get('street', None)
    city = registration_info.get('city', None)
    state = registration_info.get('state', None)
    country = registration_info.get('country', None)
    zip_code = registration_info.get('zip_code', None)
    zone = registration_info.get('zone', None)

    registrationStatus = True
    message = 'Registered Successfully'

    login = False
    details = False
    address = False

    try:
        police_login = PoliceLogin()
        police_login.pId = pId
        police_login.password = password
        police_login.save()
        login = True

        police_station_details = PoliceStationDetails()
        police_station_details.pId = pId
        police_station_details.shoName = shoName
        police_station_details.shoNumber = shoNumber
        police_station_details.save()
        details = True

        police_station_address = PoliceStationAddress()
        police_station_address.pId = pId
        police_station_address.street = street
        police_station_address.city = city
        police_station_address.state = state
        if country: police_station_address.country = country
        police_station_address.zip_code = zip_code
        police_station_address.zone = zone
        police_station_address.save()
        address = True
    
    except:
        if login:
            police_login = PoliceLogin.objects(pId=pId).first().delete()
        
        if details:
            police_station_details = PoliceStationDetails.objects(pId=pId).frst().delete()
        
        if address:
            police_station_address = PoliceStationAddress.objects(pId=pId).frst().delete()

        registrationStatus = False
        message = 'Error'
    
    registration_info['registrationStatus'] = registrationStatus
    registration_info['message'] = message

def registration(registration_info):
    pId = registration_info['pId']
    police = PoliceLogin.objects(pId=pId)
    registration_info['registrationStatus'] = None
    registration_info['message'] = None

    if len(police):
        registration_info['registrationStatus'] = False
        registration_info['message'] = 'Account Exist'

    else:
        create_account(registration_info=registration_info)
    
    return registration_info

def login(login_credentials):
    pId = login_credentials['pId']
    password = login_credentials['password']
    token = login_credentials.get('token', None)
    login_credentials['loginStatus'] = False
    login_credentials['message'] = None

    police = PoliceLogin.objects(pId=pId)

    if len(police) == 0:
        login_credentials['message'] = 'Invalid PID'

    else:
        police = police.first()

        if police.password == password:
            login_credentials['loginStatus'] = True
            login_credentials['message'] = 'Login Successfully'

        else:
            login_credentials['message'] = 'Wrong Password'
    
    return login_credentials

def registration_of_missing_child(child_details):
    pId = child_details.get('pId', None)
    firstName = child_details.get('firstName', None)
    middleName = child_details.get('middleName', None)
    lastName = child_details.get('lastName', None)
    firNo = child_details.get('firNo', None)
    firDate = child_details.get('firDate', None)
    gender = child_details.get('gender', None)
    dob = child_details.get('dob', None)
    age = child_details.get('age', None)
    dateOfMissing = child_details.get('dateOfMissing', None)
    placeOfMissing = child_details.get('placeOfMissing', None)
    complextion = child_details.get('complextion', None)
    height = child_details.get('height', None)
    weight = child_details.get('weight', None)
    built = child_details.get('built', None)
    bloodGroup = child_details.get('bloodGroup', None)
    hairColour = child_details.get('hairColor', None)
    informantName = child_details.get('informantName', None)
    informantRelation = child_details.get('informantRelation', None)
    informantEmailId = child_details.get('informantEmailId', None)
    informantPhoneNumber = child_details.get('informantPhoneNumber', None)
    informantAddress = child_details.get('informantAddress', None)
    child_face_url = child_details.get('faceURL', None)

    try: 
        face = Face()
        face_encoding = face.get_face_encoding(child_face_url)
    except:
        face_encoding = None

    registrationStatus = True
    message = 'Registered Successfully'

    details = False
    guardian_info = False
    face_register = False

    try:
        child = ChildInfo()
        child.pId = pId
        child.firstName = firstName
        if middleName: child.middleName = middleName
        if lastName: child.lastName = lastName
        child.firNo = firNo
        child.firDate = firDate
        child.gender = gender
        if dob: child.dob = dob
        if age: child.age = age
        if dateOfMissing: child.dateOfMissing = dateOfMissing
        if placeOfMissing: child.placeOfMissing = placeOfMissing
        if height: child.height = height
        if weight: child.weight = weight
        if complextion: child.complextion = complextion
        if hairColour: child.hairColour = hairColour
        if built: child.built = built
        if bloodGroup: child.bloodGroup = bloodGroup
        child.imageURL = child_face_url
        child.save()
        details = True

        child_informant_info = ChildInformantInfo()
        child_informant_info.firNo = firNo
        if informantName: child_informant_info.informantName = informantName
        if informantRelation: child_informant_info.informantRelation = informantRelation
        if informantEmailId: child_informant_info.informantEmailId = informantEmailId
        if informantPhoneNumber: child_informant_info.informantPhoneNumber = informantPhoneNumber
        if informantAddress: child_informant_info.informantAddress = informantAddress
        child_informant_info.save()
        guardian_info = True

        child_face = ChildFaceEncoding()
        child_face.firNo = firNo
        if face_encoding: child_face.face_encoding = face_encoding
        child_face.save()
        face_register = True
    
    except:
        if details:
            child = ChildInfo.objects(firNo=firNo).first().delete()
        
        if guardian_info:
            child_guradian_info = ChildInformantInfo.objects(firNo=firNo).frst().delete()
        
        if face_register:
            child_face = ChildFaceEncoding.objects(firNo=firNo).frst().delete()

        registrationStatus = False
        message = 'Error'
    
    child_details['registrationStatus'] = registrationStatus
    child_details['message'] = message
    return child_details

def updation_of_found_child(child_details):
    firNo = child_details.get('firNo', None)
    if firNo:
        child_face = ChildFaceEncoding.objects(firNo=firNo).objects().first().update(set__isFound=True)
        child_details['message'] = 'Updated Successfully'
    
    return child_details
