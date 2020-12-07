import cv2
import numpy as np

left_ear_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
right_ear_cascade = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml')


if left_ear_cascade.empty():
  raise IOError('Unable to load the left ear cascade classifier xml file')

if right_ear_cascade.empty():
  raise IOError('Unable to load the right ear cascade classifier xml file')
#3

img = cv2.imread('slike/0159.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

levo = left_ear_cascade.detectMultiScale(gray,
                                 scaleFactor=1.2,
                                 minNeighbors=1,
                                 minSize=(20,20),
                                 #maxSize=(200,200),
                                 flags=cv2.CASCADE_SCALE_IMAGE)
desno = right_ear_cascade.detectMultiScale(gray,
                                 scaleFactor=1.2,
                                 minNeighbors=1,
                                 minSize=(20,20),
                                 #maxSize=(200,200),
                                 flags=cv2.CASCADE_SCALE_IMAGE)

for (x,y,w,h) in levo: #zeleno
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

for (x,y,w,h) in desno: #modro
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)

cv2.imshow("Ear detection",img) #, cv2.resize(img,(500,500))
cv2.imwrite("Ear_detected.jpg",img)
cv2.waitKey()
cv2.destroyAllWindows()

#SLIKA 0020
#parameteri: scaleFactor = 1.05, minNeighbors=5
#overlap z annot_rect: 81.28%
#parameteri: scaleFactor = 1.08, minNeighbors=5
#overlap z annot_rect: 85.86%
#parameteri: scaleFactor = 1.10, minNeighbors=4
#overlap z annot_rect: 87.42%
#parameteri: scaleFactor = 1.15, minNeighbors=3
#overlap z annot_rect: 86.33%
#parameteri: scaleFactor = 1.2, minNeighbors=1
#overlap z annot_rect: 85.86%

#SLIKA 0159
#parameteri: scaleFactor = 1.05, minNeighbors=5
#overlap z annot_rect: 86.33%
#parameteri: scaleFactor = 1.08, minNeighbors=5
#overlap z annot_rect: 84.73%
#parameteri: scaleFactor = 1.10, minNeighbors=5
#overlap z annot_rect: 88.68%
#parameteri: scaleFactor = 1.2, minNeighbors=1
#overlap z annot_rect: 93.18%
#parameteri: scaleFactor = 1.21, minNeighbors=1
#overlap z annot_rect: 89.56%

#SLIKA 0099
#parameteri: scaleFactor = 1.05, minNeighbors=5
#overlap z annot_rect: 76.85%
#parameteri: scaleFactor = 1.2, minNeighbors=2
#overlap z annot_rect: 74.00%
#parameteri: scaleFactor = 1.07, minNeighbors=6
#overlap z annot_rect: 74.00%
#PROBLEM: lasje niso takoj zraven ušesa, zaradi tega se koža zraven ušesa zazna kot del ušesa(?)
