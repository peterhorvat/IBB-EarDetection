import cv2
import numpy as np
ear_cascade = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture(0)
while 1:
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ear = ear_cascade.detectMultiScale(gray, 1.4, 5)
  for (x,y,w,h) in ear:
      cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)

  cv2.imshow('img',img)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
      break

cap.release()
cv2.destroyAllWindows()