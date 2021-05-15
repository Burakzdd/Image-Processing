#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:38:20 2021

@author: burakzdd
"""
import cv2
import numpy as np

img = cv2.imread('/home/burakzdd/Desktop/hafta 3/lena.png')

kernel1 = np.array([[0,1,0],
                   [1,-4,1],
                   [0,1,0]])
sharp1 = cv2.filter2D(img, -1, kernel1)
zeropadding1 = cv2.copyMakeBorder(sharp1,10,10,10,10,cv2.BORDER_CONSTANT,value=0)
laplacian1 = cv2.Laplacian(zeropadding1,cv2.CV_64F)
cv2.imshow('Sol ust goruntu',laplacian1)

kernel2 = np.array([[0,-1,0],
                   [-1,4,-1],
                   [0,-1,0]])
sharp2 = cv2.filter2D(img, -1, kernel2)
zeropadding2 = cv2.copyMakeBorder(sharp2,10,10,10,10,cv2.BORDER_CONSTANT,value=0)
laplacian2 = cv2.Laplacian(zeropadding2,cv2.CV_64F)
cv2.imshow('Sol alt goruntu',laplacian2)

kernel3 = np.array([[1,1,1],
                   [1,-8,1],
                   [1,1,1]])
sharp3 = cv2.filter2D(img, -1, kernel3)
zeropadding3 = cv2.copyMakeBorder(sharp3,10,10,10,10,cv2.BORDER_CONSTANT,value=0)
laplacian3 = cv2.Laplacian(zeropadding3,cv2.CV_64F)
cv2.imshow('Sag ust goruntu',laplacian3)

kernel4 = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]])
sharp4 = cv2.filter2D(img, -1, kernel4)
zeropadding4 = cv2.copyMakeBorder(sharp4,10,10,10,10,cv2.BORDER_CONSTANT,value=0)
laplacian4 = cv2.Laplacian(zeropadding4,cv2.CV_64F)
cv2.imshow('Sag alt goruntu',laplacian4)


cv2.waitKey(0)
cv2.destroyAllWindows()
