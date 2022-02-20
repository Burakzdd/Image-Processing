#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:23:19 2021

@author: burakzdd
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('/home/burakzdd/Desktop/rapor5/coin.png', 0)
img = image.copy()

bins_num = 256

# Histogram hesaplama
hist, bin_edges = np.histogram(image, bins=bins_num)
hist = np.divide(hist.ravel(), hist.max())
 
# Bölmelerin merkezlerini hesaplama
bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

# w1(t), w2(t) nin eşiklerini(indislerini) hesaplama
weight1 = np.cumsum(hist)
weight2 = np.cumsum(hist[::-1])[::-1]

# ortanca (mean) değerlerine ulaşma
mean1 = np.cumsum(hist * bin_mids) / weight1
mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]
 
inter_class_variance = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

# Sınıflar arası varyans fonksiyonu dağeri maksimize etme
index_of_max_val = np.argmax(inter_class_variance)

otsu_esik = bin_mids[:-1][index_of_max_val]

otsu_threshold,img = cv2.threshold(img,otsu_esik,255,cv2.THRESH_BINARY)
print(otsu_threshold)
cv2.imshow("Otsu Rey and BB8",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
