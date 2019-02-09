import cv2

webcam = cv2.VideoCapture(0)

while True:
    if not webcam.isOpened():
        print('Unable to load Webcam')
        sleep(5)
        pass
    
    # Captrure frae-by-frame
    ret, frame = webcam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Gray Window', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
