import cv2
import numpy as np
import os

model1 = cv2.CascadeClassifier('Model/cascade.xml')
model2 = cv2.CascadeClassifier('Model/reducer.xml')
list_files = os.listdir(".")
for files in list_files:
	if ".jpg" in files:
		img = cv2.imread(files,1)
		result1 = model1.detectMultiScale(img, 1.05, 1,minSize = (15,15),maxSize = (45,45))
		result2 = model2.detectMultiScale(img, 1.05, 1,minSize = (15,15),maxSize = (45,45))
		for (x, y, w, h) in result1:
			cv2.rectangle(img, (x-2, y-2), (x + w+2, y + h+2), (0, 0, 255), 4)
			cv2.imwrite('result'+"/" + files,img)

		for (x, y, w, h) in result2:
			cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
			cv2.imwrite('result'+"/" + files,img)	

