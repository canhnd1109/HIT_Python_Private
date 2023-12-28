import matplotlib.pyplot as plt
import numpy as np
# x = [1, 4]
# y = [5, 9]
# a= np.array(x)
# print(a.shape)
# print(a.size)
# plt.plot(x, y)
# plt.show()


x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()