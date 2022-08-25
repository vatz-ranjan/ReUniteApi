from src.models.child_database import ChildInfo
from src.models.child_database import ChildInformantInfo
from src.models.child_database import ChildFaceEncoding

def missing_child_database():
    missing_childs = ChildFaceEncoding.objects(isFound=False).as_pymongo()
    numbers_of_missing_child = len(missing_childs)
    missing_child_details = {
        'isFound': False,
        'quantity': numbers_of_missing_child,
        'details': list()
    }

    for i in range(numbers_of_missing_child):
        curChild = dict()
        firNo = numbers_of_missing_child[i].firNo
        child_detail_length = ChildInfo.objects(firNo=firNo)
        if len(child_detail_length):
            child_detail = child_detail_length.first()
            curChild['firstName'] = child_detail.firstName
            try:
                curChild['middleName'] = child_detail.middleName
            except:
                pass
            try:
                curChild['lastName'] = child_detail.lastName
            except:
                pass
            curChild['firNo'] = child_detail.firNo
            curChild['firDate'] = child_detail.firDate
            curChild['gender'] = child_detail.gender
            try:
                curChild['dob'] = child_detail.dob
            except:
                pass
            try:
                curChild['age'] = child_detail.age
            except:
                pass
            try:
                curChild['dateOfMissing'] = child_detail.dateOfMissing
            except:
                pass
            try:
                curChild['placeOfMissing'] = child_detail.placeOfMissing
            except:
                pass
            try:
                curChild['height'] = child_detail.height
            except:
                pass
            try:
                curChild['weight'] = child_detail.weight
            except:
                pass
            try:
                curChild['complextion'] = child_detail.complextion
            except:
                pass
            try:
                curChild['built'] = child_detail.built
            except:
                pass
            try:
                curChild['bloodGroup'] = child_detail.bloodGroup
            except:
                pass
            try:
                curChild['hairColour'] = child_detail.hairColour
            except:
                pass
            try:
                curChild['imageURL'] = child_detail.imageURL
            except:
                pass
        
        child_guardian_detail_length = ChildInformantInfo.objects(firNo=firNo)
        if len(child_guardian_detail_length):
            child_guardian_detail = child_detail_length.first()
            try:
                curChild['informantName'] = child_guardian_detail.informantName
            except:
                pass
            try:
                curChild['informantRelation'] = child_guardian_detail.informantRelation
            except:
                pass
            try:
                curChild['informantEmailId'] = child_guardian_detail.informantEmailId
            except:
                pass
            try:
                curChild['informantPhoneNumber'] = child_guardian_detail.informantPhoneNumber
            except:
                pass
            try:
                curChild['informantAddress'] = child_guardian_detail.informantAddress
            except:
                pass
        
        missing_child_details['details'].append(curChild)
    
    return missing_child_details

def found_child_database():
    found_childs = ChildFaceEncoding.objects(isFound=True).as_pymongo()
    numbers_of_found_child = len(found_childs)
    found_child_details = {
        'isFound': True,
        'quantity': numbers_of_found_child,
        'details': list()
    }

    for i in range(numbers_of_found_child):
        curChild = dict()
        firNo = numbers_of_found_child[i].firNo
        child_detail_length = ChildInfo.objects(firNo=firNo)
        if len(child_detail_length):
            child_detail = child_detail_length.first()
            curChild['firstName'] = child_detail.firstName
            try:
                curChild['middleName'] = child_detail.middleName
            except:
                pass
            try:
                curChild['lastName'] = child_detail.lastName
            except:
                pass
            curChild['firNo'] = child_detail.firNo
            curChild['firDate'] = child_detail.firDate
            curChild['gender'] = child_detail.gender
            try:
                curChild['dob'] = child_detail.dob
            except:
                pass
            try:
                curChild['age'] = child_detail.age
            except:
                pass
            try:
                curChild['dateOfMissing'] = child_detail.dateOfMissing
            except:
                pass
            try:
                curChild['placeOfMissing'] = child_detail.placeOfMissing
            except:
                pass
            try:
                curChild['height'] = child_detail.height
            except:
                pass
            try:
                curChild['weight'] = child_detail.weight
            except:
                pass
            try:
                curChild['complextion'] = child_detail.complextion
            except:
                pass
            try:
                curChild['built'] = child_detail.built
            except:
                pass
            try:
                curChild['bloodGroup'] = child_detail.bloodGroup
            except:
                pass
            try:
                curChild['hairColour'] = child_detail.hairColour
            except:
                pass
            try:
                curChild['imageURL'] = child_detail.imageURL
            except:
                pass
    
    child_guardian_detail= ChildInformantInfo.objects(firNo=firNo)
    if len(child_guardian_detail):
        child_guardian_detail = child_guardian_detail.first()
        try:
                curChild['informantName'] = child_guardian_detail.informantName
        except:
            pass
        try:
            curChild['informantRelation'] = child_guardian_detail.informantRelation
        except:
            pass
        try:
            curChild['informantEmailId'] = child_guardian_detail.informantEmailId
        except:
            pass
        try:
            curChild['informantPhoneNumber'] = child_guardian_detail.informantPhoneNumber
        except:
            pass
        try:
            curChild['informantAddress'] = child_guardian_detail.informantAddress
        except:
            pass

    return curChild

        

