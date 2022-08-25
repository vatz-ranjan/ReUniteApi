from flask import Flask, request
from src.services import citizen_services
from src.services import police_services
from src.services import common_services
from src.services import dummy_services

app = Flask(__name__)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    acknowledge = dict()
    acknowledge['registrationStatus'] = False
    acknowledge['message'] = 'Error Occured'
    userType = None
    registrationDetails = None
    if request.method == 'POST':     
        try:
            userType = request.json['userType']
            registrationDetails = request.json['registrationDetails']
        except:
            pass
    
    else:
        try:
            userType = request.args.get('userType')
            registrationDetails = request.args.get('registrationDetails')
        except:
            pass
    
    try:
        if userType:
            if registrationDetails is None:
                acknowledge['message'] = 'Unexpected Data'
            elif userType == 'Citizen':
                acknowledge = citizen_services.registration(registration_info=registrationDetails)
            elif userType == 'Police':
                acknowledge = police_services.registration(registration_info=registrationDetails)
            else:
                acknowledge['message'] = 'Error Occured'
    except:
        acknowledge['message'] = 'Error Occured'
    return acknowledge

@app.route('/login', methods=['GET', 'POST'])
def signin():
    acknowledge = dict()
    acknowledge['loginStatus'] = False
    acknowledge['message'] = 'Error Occured'
    userType = None
    loginDetails = None
    if request.method == 'POST':     
        try:
            userType = request.json['userType']
            loginDetails = request.json['loginDetails']
        except:
            pass
    
    else:
        try:
            userType = request.args.get('userType')
            loginDetails = request.args.get('loginDetails')
        except:
            pass
    try:
        if userType:
            if loginDetails is None:
                acknowledge['message'] = 'Unexpected Data'
            elif userType == 'Citizen':
                acknowledge = citizen_services.login(login_credentials=loginDetails)
            elif userType == 'Police':
                acknowledge = police_services.login(login_credentials=loginDetails)
            else:
                acknowledge['message'] = 'Error Occured'
    except:
        acknowledge['message'] = 'Error Occured'
    return acknowledge

@app.route('/registrationofmissingchild', methods=['GET', 'POST'])
def registration_of_missing_child():
    acknowledge = dict()
    acknowledge['registrationStatus'] = False
    acknowledge['message'] = 'Error Occured'
    userType = None
    childDetails = None
    if request.method == 'POST':     
        try:
            userType = request.json['userType']
            childDetails = request.json['childDetails']
        except:
            pass
    
    else:
        try:
            userType = request.args.get('userType')
            childDetails = request.args.get('childDetails')
        except:
            pass
    try:
        if userType:
            if childDetails is None:
                acknowledge['message'] = 'Unexpected Data'
            elif userType == 'Police':
                acknowledge = police_services.registration_of_missing_child(child_details=childDetails)
            else:
                acknowledge['message'] = 'Error Occured'
    except:
        acknowledge['message'] = 'Error Occured'
    return acknowledge

@app.route('/updationoffoundchild', methods=['GET', 'POST'])
def updation_of_found_child():
    acknowledge = dict()
    userType = None
    childDetails = None
    if request.method == 'POST':     
        try:
            userType = request.json['userType']
            childDetails = request.json['childDetails']
        except:
            pass
    
    else:
        try:
            userType = request.args.get('userType')
            childDetails = request.args.get('childDetails')
        except:
            pass
    try:
        if userType:
            if childDetails is None:
                acknowledge['message'] = 'Error Occured'
            elif userType == 'Police':
                acknowledge = police_services.updation_of_found_child(child_details=childDetails)
            else:
                acknowledge['message'] = 'Error Occured'

    except:
        acknowledge['message'] = 'Error Occured'
    return acknowledge


@app.route('/scanimage', methods=['GET', 'POST'])
def scan_image():
    acknowledge = dict()
    acknowledge['found'] = False
    userType = None
    imageDetails = None
    if request.method == 'POST':     
        try:
            userType = request.json['userType']
            imageDetails = request.json['imageDetails']
        except:
            pass
    
    else:
        try:
            userType = request.args.get('userType')
            imageDetails = request.args.get('imageDetails')
        except:
            pass
    try:
        if userType:
            if imageDetails is None:
                acknowledge['message'] = 'Error Occured'
            elif userType == 'Citizen':
                acknowledge = citizen_services.scan_image(image_info=imageDetails)
            else:
                acknowledge['message'] = 'Error Occured'
    except:
        acknowledge['message'] = 'Error Occured'
    return acknowledge

@app.route('/missingchilddetails')
def missing_child_details():
    return common_services.missing_child_database()

@app.route('/foundchilddetails')
def found_child_details():
    return common_services.found_child_database()

@app.route('/')
def default():
    details = {
        'page': 'Default Page',
        'info': 'Shikhar khush ho jaega'
    }
    return details

@app.route('/adddummy')
def add_dummy():
    details = {
        'oneOne': 'R',
        'two': 'T'
    }
    acknowledge = dummy_services.insert(details)
    return acknowledge
    
if __name__ == '__main__':
    app.run(debug=True)