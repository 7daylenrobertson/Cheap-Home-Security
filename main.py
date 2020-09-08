import numpy as np
import cv2
from twilio.rest import Client

#DL classifier for faces
f = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#DL classifier for eyes
e = cv2.CascadeClassifier('haarcascade_eye.xml')

#Twilio User ID's
account_sid = 'AC39247dafdbfd889dc9078438294eebb8'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="An intruder might be in front of your door!",
                     from_='your Twilio number',
                     to='Your number'
                 )


cap = cv2.VideoCapture(0)
score=0
#Basically, this loop just continues to detect eyes and faces and then, once both are detected, alerts user
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = f.detectMultiScale(gray, 1.3, 5)
    

    for (x,y,w,h) in face:
        #Trigger one
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    
        eyes = e.detectMultiScale(roi_gray)

       

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            #Trigger 2 (Person Detected)
            #Send a notification to user's phone
            print(message.sid)
        


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
