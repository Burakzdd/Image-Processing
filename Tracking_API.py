#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:49:10 2021

@author: burakzdd
"""
import cv2

def ask_for_tracker():
    print("Welcome! What Tracker API would you like to use?")
    print("Enter 0 for BOOSTING: ")
    print("Enter 1 for MIL: ")
    print("Enter 2 for KCF: ")
    print("Enter 3 for TLD: ")
    print("Enter 4 for MEDIANFLOW: ")
    choice = input("Please select your tracker: ")
    
    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()
   
    return tracker
tracker = ask_for_tracker()
tracker_name = str(tracker).split()[0][1:]
cap = cv2.VideoCapture(0)
  
ret, frame = cap.read()
  
roi = cv2.selectROI(frame, False)
ret = tracker.init(frame, roi)
while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x,y,w,h) = tuple(map(int,roi))
      
    if success:
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0,255,0), 3)
       
    else :
        cv2.putText(frame, "Failure to Detect Tracking!!", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),3)
      
        cv2.putText(frame, tracker_name, (20,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),3)
        cv2.imshow(tracker_name, frame)
    if cv2.waitKey(1) & 0xFF == ord ("q"): break
cap.release()
cv2.destroyAllWindows()    
