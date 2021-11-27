import cv2

def detect_face(frame):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    try:
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                frame = frame[y-50:y+h+50, x-50:x+w+50]
                frame = cv2.resize(frame,(200,200))
            return True, frame
    except:
        pass #Will pass any errors during frame cutting for continuity because several faces brake this for some reason.
    return False, None