import cv2
import os

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognizer=cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainingData.yml')

video_capture=cv2.VideoCapture(0)

while True:
    ret ,frame=video_capture.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        label, confidence= recognizer.predict(gray[y:y+h,x:x+w])

        if confidence < 100:
            name = "Person"+str(label)
        else:
            name="Unknown"
        
        cv2.putText(frame,name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
    
    cv2.imshow("Face Recognizer",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()