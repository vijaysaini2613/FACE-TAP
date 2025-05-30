import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
while True:
    _,img= webcam.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.5, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
    cv2.imshow("Facedetection", img)
    key= cv2.waitKey(10)
    if key == 27:  # Press 'ESC' to exit
        break
webcam.release()
cv2.destroyAllWindows()