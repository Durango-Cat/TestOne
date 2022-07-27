"""
 numpy数组的测试类
"""

import numpy as np


# arr = np.arange(10)

# print(arr)

# print(arr[5])

points = np.arange(-5, 5, 0.01)
# print(points)
xs, ys = np.meshgrid(points, points)
print(xs)
print(ys)