#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:06:24 2021

@author: burakzdd
"""
import cv2
import numpy as np

img = cv2.imread('/home/burakzdd/Desktop/hafta 3/sudoku.jpg')
cv2.imshow('sudoku.jpg',img)
edges = cv2.Canny(img,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,256,0),2)

cv2.imshow('houghlines3.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


