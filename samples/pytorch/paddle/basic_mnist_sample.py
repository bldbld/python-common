import paddle
from paddle.nn import Linear
import paddle.nn.functional as F
import os
import numpy as np
import matplotlib.pyplot as plt

# 通过paddle.vision.datasets.MNIST API设置数据读取器
# 飞桨提供了多个封装好的数据集API，涵盖计算机视觉、自然语言处理、推荐系统等多个领域，帮助读者快速完成深度学习任务。
# 如在手写数字识别任务中，通过paddle.vision.datasets.MNIST可以直接获取处理好的MNIST训练集、测试集，飞桨API支持如下常见的学术数据集
train_dataset = paddle.vision.datasets.MNIST(mode='train')

# 通过如下代码读取任意一个数据内容，观察打印结果。
train_data0 = np.array(train_dataset[999][0])
train_label_0 = np.array(train_dataset[999][1])

# 显示第一batch的第一个图像
import matplotlib.pyplot as plt
plt.figure("Image") # 图像窗口名称
plt.figure(figsize=(5,5))
plt.imshow(train_data0, cmap=plt.cm.binary)
plt.axis('on') # 关掉坐标轴为 off
plt.title('image') # 图像题目
plt.show()

print("图像数据形状和对应数据为:", train_data0.shape)
print("图像标签形状和对应数据为:", train_label_0.shape, train_label_0)
print("\n打印第一个batch的第一个图像，对应标签数字为{}".format(train_label_0))
