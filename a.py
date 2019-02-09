import cv2

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

webcam = cv2.VideoCapture(0)

while True:
    if not webcam.isOpened():
        print('Unable to load Webcam')
        sleep(5)
        pass
    
    # Captrure frae-by-frame
    ret, frame = webcam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Window', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
