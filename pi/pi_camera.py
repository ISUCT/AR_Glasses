from picamera import PiCamera
from time import sleep

# this is only an example of python pi camera work

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('./picture.jpg')
camera.stop_preview()