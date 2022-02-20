#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:48:12 2021

@author: burakzdd
"""
import cv2
#video oynatılır
cap = cv2.VideoCapture("/home/burakzdd/Desktop/görüntü/iha.mp4")
#Arkaplan çıkarılır(iki görüntü birbirinden de denilebilir) 
#Eğer detectShadows True ise gölgeler gösterilir
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)


while(1):
    #video okunur
    ret,frame = cap.read()
    #yukarıda oluşturulan maske görüntüye uygulanır
    fgmask = fgbg.apply(frame)
    #gürültüleri kaldırmak için blur uygulanır
    median = cv2.medianBlur(fgmask,3)
    #hareketli görüntüyü rgb görüntü üzerinde işaretlemek (şekil içine almak) için
    #findCountours komutunu kullanıyoruz
    (contours,hierarchy)=cv2.findContours(median.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        #eğer countour sayısı az ise (sınır 500 aldık)devam edip çok ise dikdörtgen çizecek
        #kısaca hassasiyetini ayarladık
        if cv2.contourArea(c) < 500:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    
    #iki görüntüde bastırılır
    cv2.imshow('arka plan ayrilmis',median);
    cv2.imshow('nesne takip',frame);
    #durdurma bekleme komutları
    k =cv2.waitKey(1) & 0xff
    if  k==27:
        break
    
cap.release()
cv2.destroyAllWindows()    


