import cv2
from helpers.detect_face import detect_face
from helpers import pass_face_helper
from helpers import pass_face_helper
from converters.image_converter import convert_image_to_base64
from helpers import serial_helper

camera = cv2.VideoCapture(0)

serial_helper.open_serial_connection()

face_not_detected_count = 0
face_not_detected_threshold = 100

while(True):
    ret, frame = camera.read()
    is_detected, face_crop = detect_face(frame)
    print(face_not_detected_count)
    if is_detected:
        face_not_detected_count = 0
        fc_base64 = convert_image_to_base64(img=face_crop)
        person_name = pass_face_helper.get_person(fc_base64)
        serial_helper.send_data_to_arduino(person_name)
    else:
        serial_helper.send_data_to_arduino('none') #Specifically lower-case none because gods said so
        face_not_detected_count += 1
        if face_not_detected_count >= face_not_detected_threshold:
            serial_helper.send_data_to_arduino('Undetected')
            face_not_detected_count = 0