#!/usr/local/bin python
#Author: Xiaohong Zhao
#Date: 2017.11.3

import libpysunergy
import cv2
from os import listdir
from os.path import isfile, join

pic_dir = './pics/'
res_dir = './results/'

#image list
imagelist = [f for f in listdir(pic_dir) if isfile(join(pic_dir, f))]

#load yolo_coco detector
net1,names1 = libpysunergy.load("data/coco.data", "cfg/yolo.cfg", "weights/yolo.weights")
threshold = 0.24
cfg_size = (608,608) #same as network input

#process images
for image in imagelist:
	print image
	#load and convert image
	img = cv2.imread(pic_dir + image)
	(h,w,c) = img.shape
	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img_input = cv2.resize(img_rgb, cfg_size)

	#dets returns {py_names[class], prob, left, right, top, bot}
	dets = libpysunergy.detect(img_input.data, w, h, c, threshold, net1, names1)

	#crop cars
	obj_num = len(dets)
	count = 0
	for i in range(0, obj_num):
		if dets[i][0] == "car":
			(x0,x1,y0,y1) = dets[i][2],dets[i][3],dets[i][4],dets[i][5]
			img_car = img[y0:y1, x0:x1].copy()
			print "car detected!"
			cv2.imwrite( res_dir + image + '_' + str(count) + '.jpg',img_car)
			count += 1

libpysunergy.free(net1)		
