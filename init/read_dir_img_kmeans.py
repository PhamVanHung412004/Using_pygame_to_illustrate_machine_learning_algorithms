import os
import cv2
from sklearn.cluster import KMeans
import numpy
path = "D:/init/img"

list_img = os.listdir(path)     

# print(list_img)

# for i in list_img
save_img = "D:/init/list_img/"
# i = 1
list_name_img = []
index_img = 1
for img in list_img:
    path_new = path + "/" + img
    image = cv2.imread(path_new)
    width = image.shape[0]
    height = image.shape[1]
    image = image.reshape(width*height,3)
    dau_cham = img.index(".")
    name = img[dau_cham:]
    list_digital_index_img = []
    # print(name)
    for k in range(1,9):
        kmeans = KMeans(n_clusters=k).fit(image)
        labels = kmeans.predict(image)
        clusters = kmeans.cluster_centers_
        image1 = numpy.zeros((width,height,3), dtype=numpy.uint8)
        index = 0
        for i in range(width):
            for j in range(height):
                label_of_pixel = labels[index]
                image1[i][j] = clusters[label_of_pixel]
                index += 1
        list_digital_index_img.append(index_img)
        cv2.imwrite(save_img + str(index_img) + name,image1)
        index_img += 1
    list_name_img.append(list_digital_index_img)
print(list_name_img)