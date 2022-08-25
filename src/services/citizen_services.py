import pickle
from MissingChild.src.face_detection import compare_faces as CompareFace
from src.models.citizen_database import CitizenLogin
from src.models.citizen_database import CitizenDetails
from src.models.citizen_database import CitizenAddress
from src.models.child_database import ChildFaceEncoding
from src.services import common_services

def create_account(registration_info):
    emailId = registration_info.get('emailId', None)
    password = registration_info.get('password', None)
    firstName = registration_info.get('firstName', None)
    middleName = registration_info.get('middleName', None)
    lastName = registration_info.get('lastName', None)
    phoneNumber = registration_info.get('phoneNumber', None)
    governmentId = registration_info.get('governmentId', None)
    street = registration_info.get('street', None)
    city = registration_info.get('city', None)
    state = registration_info.get('state', None)
    country = registration_info.get('country', None)
    zip_code = registration_info.get('zip_code', None)

    registrationStatus = True
    message = 'Registered Successfully'

    login = False
    details = False
    address = False

    try:
        citizen_login = CitizenLogin()
        citizen_login.emailId = emailId
        citizen_login.password = password
        citizen_login.save()
        login = True

        citizen_details = CitizenDetails()
        citizen_details.emailId = emailId
        citizen_details.firstName = firstName
        if middleName: citizen_details.middleName = middleName
        if lastName: citizen_details.lastName = lastName
        citizen_details.phoneNumber = phoneNumber
        if governmentId: citizen_details.governmentId = governmentId
        citizen_details.save()
        details = True

        citizen_address = CitizenAddress()
        citizen_address.emailId = emailId
        citizen_address.street = street
        citizen_address.city = city
        citizen_address.state = state
        if country: citizen_address.country = country
        citizen_address.zip_code = zip_code
        citizen_address.save()
        address = True
    
    except:
        if login:
            citizen_login = CitizenLogin.objects(emailId=emailId).first().delete()
        
        if details:
            citizen_details = CitizenDetails.objects(emailId=emailId).frst().delete()
        
        if address:
            citizen_address = CitizenAddress.objects(emailId=emailId).frst().delete()

        registrationStatus = False
        message = 'Error'
    
    registration_info['registrationStatus'] = registrationStatus
    registration_info['message'] = message

def registration(registration_info):
    emailId = registration_info['emailId']
    citizen = CitizenLogin.objects(emailId=emailId)
    registration_info['registrationStatus'] = None
    registration_info['message'] = None

    if len(citizen):
        registration_info['registrationStatus'] = False
        registration_info['message'] = 'User Exist'

    else:
        create_account(registration_info=registration_info)
    
    return registration_info

def login(login_credentials):
    emailId = login_credentials['emailId']
    password = login_credentials['password']
    token = login_credentials.get('token', None)
    login_credentials['loginStatus'] = False
    login_credentials['message'] = None

    citizens = CitizenLogin.objects(emailId=emailId)

    if len(citizens) == 0:
        login_credentials['message'] = 'Invalid EmailId'

    else:
        citizen = citizens.first()

        if citizen.password == password:
            login_credentials['loginStatus'] = True
            login_credentials['message'] = 'Login Successfully'

        else:
            login_credentials['message'] = 'Wrong Password'
    
    return login_credentials

def update_profile(updation_details):
    pass

def scan_image(image_info):
    child_info = {
        'found': False,
        'confidence': 0,
        'message': 'Not Present in Database'
    }
    url = image_info.get('URL', None)
    face_encodings = []
    try:
        face_encoding_database = ChildFaceEncoding.objects(isFound=False).as_pymongo()
        length_faces = len(face_encoding_database)
        face_encodings = [face_encoding_database[index]['face_encoding'] for index in range(length_faces)]
        face_encodings = list(map(pickle.loads, face_encodings))
        child_firNos = [face_encoding_database[index]['firNo'] for index in range(length_faces)]
    except:
        face_encodings = []
        
    if url:
        cface = CompareFace()
        child_update = cface.compare_face(url, face_encodings)
        if child_update['index'] > -1:
            firNo = child_firNos[child_update['index']]
            curChild = common_services.get_child_details(firNo=firNo)
            child_info['details'] = curChild
    
    else:
        message = 'No Faces Found'
    
    return child_info


