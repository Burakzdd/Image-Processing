# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2

img = cv2.imread('/home/burakzdd/Desktop/work1/lena.png')
cv2.imshow('image', img)
graylena = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray lena picture",graylena)
cv2.waitKey(0)
cv2.destroyAllWindows()
