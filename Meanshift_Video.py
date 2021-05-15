#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:02:18 2021
@author: burakzdd
"""
import cv2
import numpy as np

videoCapture = cv2.VideoCapture("/home/burakzdd/Desktop/görüntü/iha.mp4")

ret, frame = videoCapture.read()
rows, cols = frame.shape[:2]

#Görüntü üzerinde Mean Shift için bir alan belirlenir
#Bu koordinatlar ağırlıklı ortalaması belirlenecek olan dörtgen alanıdır
w = 300
h = 200
col = int((cols - w) / 2)
row = int((rows - h) / 2)
shiftWindow = (col, row, w, h)

#Parlaklık ve renk dağılımlarını dengelemek için bir maskeleme alanı oluşturulur ve bu alan üzerinde histogram eşitleme yapılır
roi = frame[row:row + h, col:col + w]
roiHsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

lowLimit = np.array((0., 60., 32.))
highLimit = np.array((180., 255., 255.))
mask = cv2.inRange(roiHsv, lowLimit, highLimit)

roiHist = cv2.calcHist([roiHsv], [0], mask, [180], [0, 180])
cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)


#Algoritmanın kendi içerisinde kaydırma/hesaplama işlemini kaç defa yapacağı belirlenir

terminationCriteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS , 10, 1)

while True:
    ret , frame = videoCapture.read()

    #video içerisinde öncelikli  HSV  renk uzayı üzerinde histogram alıp histogram back projection(geri gösterim) 
    #yapacağız ve tüm görüntü üzerinde istediğimiz yerin segmentlerini bulacağız.
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backprojectedFrame = cv2.calcBackProject([frameHsv], [0], roiHist, [0, 180], 1)

    # karanlıkta kalan alanlar maskelenir
    mask = cv2.inRange(frameHsv, lowLimit, highLimit)
    backprojectedFrame &= mask

    # mean shift algoritması başalatılır
    ret, shiftWindow = cv2.meanShift(backprojectedFrame, shiftWindow, terminationCriteria)

    #Col, row artık mean shift ile elde edilen alandır
    col, row = shiftWindow[:2]

    #Görüntü üzerinde tespit edilen alan çizdirilir
    frame = cv2.rectangle(frame, (col, row), (col + w, row + h), (255,255,0), 4)
    cv2.imshow('Mean Shift iha', frame)
    
    if cv2.waitKey(1) & 0xFF == ord ("q"): break

videoCapture.release()
cv2.destroyAllshiftWindows()


