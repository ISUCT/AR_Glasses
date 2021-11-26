import cv2
from helpers.detect_face import detect_face
from helpers import pass_face_helper
from converters.image_converter import convert_image_to_base64

camera = cv2.VideoCapture(0)

def quick_save_file(bytes):
    with open("Output.txt", "w") as text_file:
        text_file.write(str(bytes))

while(True):
    ret, frame = camera.read()
    is_detected, face_crop = detect_face(frame)
    if is_detected:
        fc_base64 = convert_image_to_base64(img=face_crop)
        quick_save_file(fc_base64)
        pass_face_helper.send_passface_request(fc_base64)
    pass