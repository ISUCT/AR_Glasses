from os import path
import config
from converters import image_converter
from time import sleep

if config.ENVIRONMENT_STATE == "DEBUG":
    import cv2
else:
    import picamera

def capture_image_debug():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()
    return frame

def capture_image_pi():
    pi_camera = picamera.PiCamera()
    pi_camera.start_preview()
    sleep(5)
    pi_camera.capture('./picture.jpg')
    pi_camera.stop_preview()

if config.ENVIRONMENT_STATE == 'DEBUG':
    captured_frame = capture_image_debug()
    img_enc = image_converter.convert_image_to_base64(img=captured_frame)
else:
    capture_image_pi()
    img_enc = image_converter.convert_image_to_base64(path='./picture.jpg')
