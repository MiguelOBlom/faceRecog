#!/usr/bin/env python3

# Prints the number of detected faces in a given <image> given a cascade on <cascPath>

import cv2
import sys
import numpy as np

from PIL import Image, ImageOps

import time
import matplotlib.pyplot as plt
import matplotlib.patches as patches

sf=4

if len(sys.argv) != 3:
	print("Usage: " + sys.argv[0] + " <cascPath> <image>")
	exit()

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

img = cv2.imread(sys.argv[2], cv2.IMREAD_UNCHANGED) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (int(gray.shape[1]/sf), int(gray.shape[0]/sf)))

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=6,
    minSize=(int(150/sf), int(150/sf)), # Images are of size 512×768 
    flags=cv2.CASCADE_SCALE_IMAGE
)

fig, ax = plt.subplots()
ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
for (x, y, w, h) in faces:
        rect = patches.Rectangle((x*sf, y*sf), w*sf, h*sf, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

print(len(faces))