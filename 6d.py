#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:56:56 2021

@author: burakzdd
"""

import numpy as np
import cv2
img = np.zeros((200,200,3), np.uint8)
cv2.rectangle (img,(20,20), (180,180), (100,100,100), -1)
cv2.rectangle (img,(40,40), (160,160), (150,150,150), -1)
cv2.rectangle (img,(60,60), (140,140), (200,200,200), -1)
cv2.rectangle (img,(80,80), (120,120), (256,256,256), -1)
mean = 0
var = 3
sigma = var ** 0.5
gaussian = np.random.normal(mean, sigma, (200, 200)) #  np.zeros((224, 224), np.float32)

noisy_image = np.zeros(img.shape, np.float32)

if len(img.shape) == 2:
    noisy_image = img + gaussian
else:
    noisy_image[:, :, 0] = img[:, :, 0] + gaussian
    noisy_image[:, :, 1] = img[:, :, 1] + gaussian
    noisy_image[:, :, 2] = img[:, :, 2] + gaussian

cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
noisy_image = noisy_image.astype(np.uint8)

cv2.imshow("img", img)
cv2.imshow("gaussian", gaussian)
cv2.imshow("noisy", noisy_image)
cv2.imshow("noisyy", noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

