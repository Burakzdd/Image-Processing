#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:10:44 2021

@author: burakzdd


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/home/burakzdd/Desktop/hafta 3/castle.png',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/home/burakzdd/Desktop/hafta 3/castle.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()