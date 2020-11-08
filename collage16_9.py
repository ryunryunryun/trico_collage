# This creates collage of TRICO

import cv2
import datetime 
import os
import itertools
import numpy as np
import math

dateList = []
TRICOfiles = os.listdir("TRICO")

for f in TRICOfiles:
	if (f == ".DS_Store"):
		continue

	d = f.replace(".jpg", "")
	dateFormatted = [f, datetime.datetime.strptime(d, "%Y-%m-%d %H-%M-%S")]


	dateList.append(dateFormatted)


# sort according to date
sortedDate = sorted(dateList, key = lambda d: d[1])

"""
# make all images 270 * 320 (crop if needed)
for i in range(200):
	print(i)
	im = cv2.imread("TRICO/" + sortedDate[i][0])
	h, w, ch = im.shape

	if (w / h > 32/27):
		im_resized = im[0 : h, round(w / 2) - round(h * 16 / 27) : round(w / 2) + round(h * 16 / 27), :]
		im_resized = cv2.resize(im_resized, dsize = (320, 270))
	else: 
		im_resized = im[round(h / 2) - round(w * 27 / 64) : round(h / 2) + round(w * 27 / 64), 0 : w, :]
		im_resized = cv2.resize(im_resized, dsize = (320, 270))

	cv2.imwrite("TRICO 16-9 modified/" + str(i) + ".jpg", im_resized, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
"""


# make collage 
collage = np.zeros((12 * 270, 18 * 320, 4))
 
for i in range(90):
	print(i)
	im = cv2.imread("TRICO 16-9 modified/" + str(i) + ".jpg")
	leftTopCol = 18 * 320 - (i % 18 + 1) * 320
	leftTopRow = 12 * 270 - (math.floor(i / 18) + 1) * 270

	for j in range(270):
		for k in range(320):
			collage[leftTopRow + j][leftTopCol + k][0] = im[j][k][0]
			collage[leftTopRow + j][leftTopCol + k][1] = im[j][k][1]
			collage[leftTopRow + j][leftTopCol + k][2] = im[j][k][2]
			collage[leftTopRow + j][leftTopCol + k][3] = 255


for i in range(90, 110):
	print(i)
	im = cv2.imread("TRICO 16-9 modified/" + str(i) + ".jpg")
	if (i % 10 < 5):
		leftTopCol = 18 * 320 - (i % 10 + 1) * 320
		leftTopRow = 270 * 7 - (math.floor((i - 90) / 10) + 1) * 270
	else:
		leftTopCol = 5 * 320 - ((i - 5) % 10 + 1) * 320
		leftTopRow = 270 * 7 - (math.floor((i - 95) / 10) + 1) * 270

	for j in range(270):
		for k in range(320):
			collage[leftTopRow + j][leftTopCol + k][0] = im[j][k][0]
			collage[leftTopRow + j][leftTopCol + k][1] = im[j][k][1]
			collage[leftTopRow + j][leftTopCol + k][2] = im[j][k][2]
			collage[leftTopRow + j][leftTopCol + k][3] = 255


for i in range(110, 200):
	print(i)
	im = cv2.imread("TRICO 16-9 modified/" + str(i) + ".jpg")
	leftTopCol = 320 * 18 - ((i - 110) % 18 + 1) * 320
	leftTopRow = 270 * 5 - (math.floor((i - 110) / 18) + 1) * 270

	for j in range(270):
		for k in range(320):
			collage[leftTopRow + j][leftTopCol + k][0] = im[j][k][0]
			collage[leftTopRow + j][leftTopCol + k][1] = im[j][k][1]
			collage[leftTopRow + j][leftTopCol + k][2] = im[j][k][2]
			collage[leftTopRow + j][leftTopCol + k][3] = 255


cv2.imwrite("collage16-9.png", collage)









