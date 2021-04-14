#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 00:32:26 2021

@author: burakzdd
"""

import numpy as np
import cv2
img =  cv2.imread('/home/burakzdd/Desktop/rapor5/bb8.jpg')
cv2.imshow('Orjinal BB8',img)
#görüntü tekrar konumlandırılır
Z = img.reshape((-1,3))
# veri tipi np.float32 'ye dönüştürülür
Z = np.float32(Z)
# kriterleri, küme sayısı (K) tanımlanır ve k ortalama(means)değerleri uygulanır
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Grüntü tekraradan eski tipine (uint8'e) dönüştürülür ve görüntünün kümelendirilmiş hali oluşturulur
center = np.uint8(center)
res = center[label.flatten()]
KMimg = res.reshape((img.shape))
cv2.imshow('K-Means BB8',KMimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

