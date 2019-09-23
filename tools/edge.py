from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse
import cv2,sys,os
import numpy as np
from matplotlib import pyplot as plt
# p edge.py --input_dir  --output_dir
parser = argparse.ArgumentParser()
parser.add_argument("--input_dir", required=True, help="path to folder containing images")
parser.add_argument("--output_dir", required=True, help="output path")
a = parser.parse_args()




for img_path in os.listdir(a.input_dir):
	print(a.input_dir+'/'+img_path)

	# img = cv2.imread(a.input_dir+'/'+img_path,0)
	# print(a.input_dir+img_path)
	img = cv2.imread(a.input_dir+'/'+img_path, cv2.IMREAD_GRAYSCALE)
	# img = cv2.GaussianBlur(img, (11, 11), 0)
	# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
	# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
	laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
	# canny = cv2.Canny(img, 100, 150)
	# cv2.imshow("Image", img)
	# cv2.imshow("Sobelx", sobelx)
	# cv2.imshow("Sobely", sobely)
# 	cv2.imshow("Laplacian", laplacian)
	# cv2.imshow("Canny", canny)

	# # Converting the image to grayscale.
	# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# # Using the Canny filter to get contours
	# edges = cv2.Canny(gray, 20, 30)
	# # Using the Canny filter with different parameters
	# # Stacking the images to print them together
	# # For comparison
	# images = np.hstack((gray, edges, edges_high_thresh))

	# # Display the resulting frame
	# cv2.imshow('Frame', canny_images)



	edges_high_thresh = cv2.Canny(img, 60, 120)
	edges = cv2.Canny(img,100,200)
	# cv2.imshow("edges",edges)
	# img_not = cv2.bitwise_not(edges)
	img_not_high = cv2.bitwise_not(edges_high_thresh)
	# cv2.imshow("Invert1",img_not)
	# plt.subplot(121),plt.imshow(img,cmap = 'gray')
	# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	# plt.imshow(img_not,cmap = 'gray')
# 	plt.imshow(img_not_high,cmap = 'gray')
	# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
	# Negative
	# write
	# cv2.imshow("Invert1",edges_neg)
	outfile=a.output_dir+'/'+img_path
	print(outfile)
	cv2.imwrite(outfile, img_not_high)
	# plt.show()



