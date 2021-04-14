#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:28:40 2021

@author: burakzdd
"""
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
   
def hist_plot(img): 
     
    count =[] 
    r = [] 
      
    # loop to traverse each intensity  
    # value 
    for k in range(0, 256): 
        r.append(k) 
        counttut = 0

        for i in range(m): 
            for j in range(n): 
                if img[i, j]== k: 
                    counttut+= 1
        count.append(counttut) 
          
    return (r, count) 
  
img = cv2.imread('/home/burakzdd/Desktop/hafta 3/castle.png', 0) 
  
m, n = img.shape 
r1, count1 = hist_plot(img) 
  
plt.stem(r1, count1) 
plt.xlabel('yoğunluk değeri') 
plt.ylabel('pixel sayısı') 
plt.title('Kale görüntüsünün histogramı')
plt.show()

