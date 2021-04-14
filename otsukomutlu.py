#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:33:46 2021

@author: burakzdd
"""
import cv2
img =  cv2.imread('/home/burakzdd/Desktop/rapor5/bb8.jpg',0)

deger1,thimg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
deger2,otsuimg = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Binary Thresh Rey and BB",thimg)
cv2.imshow("Otsu Rey and BB8",otsuimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


