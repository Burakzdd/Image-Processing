#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:40:38 2021

@author: burakzdd
"""

import cv2
import numpy as np

img = cv2.imread('/home/burakzdd/Desktop/hafta 3/trees.bmp',0)
equ = cv2.equalizeHist(img)
cv2.imshow('Orjinal goruntu',img)
cv2.imshow('Esitlenen goruntu',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()

