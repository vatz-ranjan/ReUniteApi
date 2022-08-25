from src.models.dummy_database import DummyDetails

def insert(dummy_details):
    dummy_details['Success'] = False
    dummy_obj = DummyDetails()
    dummy_obj.oneOne = dummy_details['oneOne']
    dummy_obj.two = dummy_details['two']
    dummy_obj.save()
    dummy_details['Success'] = True

    return dummy_details