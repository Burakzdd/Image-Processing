#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:55:20 2021

@author: burakzdd
"""

import cv2
import numpy as np

img= cv2.imread("/home/burakzdd/Desktop/work1/lena.png")

# colorReduce()
div = 64
quantized = img // div * div + div // 2
cv2.imwrite('Lena_2bitquantized.jpg', quantized)
cv2.imshow('Lena_2bitquantized.jpg', quantized)

cv2.waitKey(0)
cv2.destroyAllWindows()
