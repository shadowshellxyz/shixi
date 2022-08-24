#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

import pandas as pd

import matplotlib.mlab as mlab

import matplotlib.pyplot as plt

np.random.seed(0)

num_bins = 50

mu = 100

sigma = 15

x = mu + sigma * np.random.randn(500)

#np.random.rand(n) 产生标准正态分布， 即均值为0 标准差为1 的高斯分布 扥同于 np.random.normal(0, 1, n)

# x = mu + sigma * np.random.randn(500) 是产生500个均值为100， 方差为15 的随机数

# 等于 x = np.random.normal(100, 15, 500)

fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, num_bins, normed=1)

#这里ax.hist()即是画柱状图的函数

#x 为数据，num_bins为分隔的段数

plt.show()

