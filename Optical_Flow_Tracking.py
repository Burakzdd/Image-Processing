#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:43:06 2021
@author: burakzdd
"""
import numpy as np
import cv2

cap = cv2.VideoCapture('/home/burakzdd/Desktop/görüntü/trafik.mp4')
# ShiTomasi Köşe tesbiti için parametlereler oluşturulur
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
# Lucas kanade optical flow için parametreler oluşturulur
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
# Restgele renkler oluşturulur
color = np.random.randint(0,255,(100,3))

#İlk kareyi alır ve içindeki köşeleri bulur
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Çizim amacıyla bir maske görüntüsü oluşturulur
mask = np.zeros_like(old_frame)

while(1):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #  optical flow(optik akış) hesaplanır 
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Sağlam/iyi noktalar seçilir
    good_new = p1[st==1]
    good_old = p0[st==1]
    
    # izleme çizgileri çizilir
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(frame,mask)
    #görüntü bastırılır.
    cv2.imshow('frame',img)
    #ESC tuşu ile çıkış sağlanır
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # Önceki kare ve noktalar güncellenir
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()
