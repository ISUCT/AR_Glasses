import requests
import json
from transliterate import translit

def get_passface_id(base64_image):
    r = requests.post('http://10.0.7.43:4000/recognitionTest', json={'media': base64_image})
    json_data = r.json()
    return json_data['personId']

def create_user_map_from_json():
    with open('pi/helpers/response.json') as json_file:
        return json.load(json_file)

def get_name_by_id(_id):
    user_map = create_user_map_from_json()
    for user in user_map:
        if user["id"] == _id:
            return '{} {}'.format(user["name"], user["surname"])

def transliterate_name(name):
    return translit(name, 'ru', reversed=True)

def get_person(base64_image):
    person_id = get_passface_id(base64_image)
    if person_id:
        person_fullname = get_name_by_id(person_id)
        transliterated_fullname = transliterate_name(person_fullname)
        return transliterated_fullname
    return "Unknown person"
