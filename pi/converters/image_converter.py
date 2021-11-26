import base64
import cv2

def convert_image_to_base64(path=None, img=None):
    if path:
        image = open(path, 'rb')
        image_read = image.read()
        encoded_image = base64.b64encode(image_read)
        encoded_image = encoded_image.decode('utf-8')
    if img is not None:
        etval, buffer = cv2.imencode('.jpg', img)
        encoded_image = base64.b64encode(buffer)
        encoded_image = encoded_image.decode('utf-8')
    return encoded_image