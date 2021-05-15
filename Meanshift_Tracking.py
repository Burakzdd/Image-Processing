#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 01:16:33 2021

@author: burakzdd
"""

import cv2
import numpy as np
#kamerayı açalım
cap = cv2.VideoCapture(0)

#bir tane frame okunur (yüz tespiti yapılır)
ret, frame = cap.read()
#Eğer ilk çalıştırıldığında bir yüz bulamazsa nesne tespiti yapılmaz ve takip başlatılmazl
if ret == False:
    print("Uyarı")
#detetion     
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_rects = face_cascade.detectMultiScale(frame)
    
(face_x, face_y, w, h) = tuple(face_rects[0])
track_window = (face_x, face_y, w, h) #meanshift algoritması girdisi

#region of interest
roi = frame[face_y:face_y + h, face_x : face_x + w] #roi =face
#rio yi rgb den hsv ye dönüştüryoruz
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180]) #takip için histogram gerekli
cv2.normalize(roi_hist , roi_hist ,0 ,255, cv2.NORM_MINMAX)

#takip için gerekli durdurma kriterleri
#count =  hesaplanacak maksimum öge sayısı
#epsilon = yinelemeli algoritmalarda gerkelşi doğruluk ve değişiklik
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5, 1)

while True:
    ret, frame = cap.read()
    
    if ret:
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #histogramı bir görüntüde bulmak için kullanıyoruz
        #bir görüntü modelindeki piksel dağılımlarının görüntünün histogramına ne kadar uyguğunu inceliyoruz (piksel karşılaştırma)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
        
        #track_window nesneyi takip etmek için döngüde sürekli bize nesnenin konumunu döndürecek
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # x,y başlangıç konumu ; w,h genişlik ve yükseklik
        x,y,w,h = track_window
        #burda framein üzerine belirlenen konumlarda çerçeveyi yerleştiriyoruz
        img2 = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),5)
        cv2.imshow("Burak'i Takip Et ", img2)
        
        #eğer q harfine basarsak çıkacak
        if cv2.waitKey(1) & 0xFF == ord ("q"): break
    
   
cap.release()
cv2.destroyAllWindows()    


