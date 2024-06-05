import matplotlib.pyplot as cv2
from sklearn.cluster import KMeans
import cv2
import numpy

path = "C:/Users/LAPTOP/Downloads/init/img/add1.jpg"

file_img = "C:/Users/LAPTOP/Downloads/init/list_img/img.png"

image = cv2.imread(path)

# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyWindow()

width = image.shape[0]
height = image.shape[1]

# print(image.shape)
image = image.reshape(width*height,3)

kmeans = KMeans(n_clusters=4).fit(image)

labels = kmeans.predict(image)
clusters = kmeans.cluster_centers_

# print(labels)
# print(clusters)

img2 = numpy.zeros((width,height,3), dtype=numpy.uint8)

index = 0
for i in range(width):
	for j in range(height):
		label_of_pixel = labels[index]
		img2[i][j] = clusters[label_of_pixel]
		index += 1

cv2.imwrite(file_img, img2)
# cv2.imshow(img2)
# cv2.show()

