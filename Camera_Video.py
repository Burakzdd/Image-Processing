#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:39:05 2021

@author: burakzdd
"""

import numpy as np
import cv2

cap= cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,255)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    
