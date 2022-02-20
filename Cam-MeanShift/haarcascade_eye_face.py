#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:46:55 2021
@author: burakzdd
"""
import cv2 
import numpy as np 

# Yüz ve gözler için kademeli sınıflandırıcıları çağrıldı
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml') 

# yüzü algılamak için bir fonksiyon oluşturuldu
def adjusted_detect_face(img): 
	
	face_img = img.copy() 
	
	face_rect = face_cascade.detectMultiScale(face_img, scaleFactor = 1.2, minNeighbors = 5) 
	for (x, y, w, h) in face_rect: 
		cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
	return face_img 

# göz algılamak için bir fonksiyon oluşturuldu
def detect_eyes(img): 
	
	eye_img = img.copy()	 
	eye_rect = eye_cascade.detectMultiScale(eye_img, scaleFactor = 1.2, minNeighbors = 5)	 
	for (x, y, w, h) in eye_rect: 
		cv2.rectangle(eye_img, (x, y), (x + w, y + h), (255, 255, 255), 10)		 
	return eye_img 

#görüntü okundu
img = cv2.imread('/home/burakzdd/Desktop/görüntü/luke.jpg') 

#görüntü tespit fonksiyonlarına gönderildi
face = adjusted_detect_face(img) 
eyes_face = detect_eyes(face) 

#yeni görüntü bastırıldı
cv2.imshow("img",eyes_face)
cv2.waitKey(0)
cv2.destroyAllWindows()    

