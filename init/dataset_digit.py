from sklearn import datasets
# from sklearn.datasets import load_digits
# from random import randint
import numpy as np
import matplotlib.pyplot as plt
import cv2


datas = datasets.load_digits()

data = datas.data
labels = datas.target

img = data.images[0]
print(type(img))
# plt.imshow(img)
# plt.show()
# print(data[0])
# print(len(data))
# print(len(labels))





# import matplotlib.pyplot as plt
# import numpy as np

# Tạo một lưới 2x2 subplots
# fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# # Tạo dữ liệu hình ảnh ngẫu nhiên
# image1 = np.random.rand(100, 100)
# image2 = np.random.rand(100, 100)
# image3 = np.random.rand(100, 100)
# image4 = np.random.rand(100, 100)
# print(type(image1))
# cv2.imshow("img",data[0][1])
# cv2.waitKey(0)
# # plt.imshow(data[0])
# # plt.show()
# # print(type(data[0]))
# # # Hiển thị từng hình ảnh trên các subplot
# # axes[0, 0].imshow(data[0])
# # axes[0, 0].set_title('Image 1')
# # axes[0, 1].imshow(image2, cmap='plasma')
# # axes[0, 1].set_title('Image 2')
# # axes[1, 0].imshow(image3, cmap='inferno')
# # axes[1, 0].set_title('Image 3')
# # axes[1, 1].imshow(image4, cmap='magma')
# # axes[1, 1].set_title('Image 4')

# # # Ẩn các trục
# # for ax in axes.flat:
# #     ax.axis('off')

# # # Tự động điều chỉnh khoảng cách giữa các subplot
# # plt.tight_layout()

# # # Hiển thị hình ảnh
# # plt.show()
