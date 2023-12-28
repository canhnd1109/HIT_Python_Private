import numpy as np

# Khởi tạo mảng numpy a (1-D) với n phần tử ngẫu nhiên trong khoảng từ [1, 14]
n = 10
a = np.random.randint(1, 15, size=n)

# Khởi tạo mảng numpy b với 100 số chẵn đầu tiên
b = np.arange(2, 202, 2)

# Khởi tạo ma trận numpy c có kích thước nxn với 100 phần tử 0
n = 10
c = np.zeros((n, n))

# Khởi tạo ma trận đơn vị d có kích thước nxn
d = np.eye(n)

# Khởi tạo ma trận đường chéo e với các giá trị trên đường chéo là mảng a
e = np.diag(a)

# In ra các ma trận và thông số
print("Mảng a:")
print(a)
print("ndim (số chiều):", a.ndim)
print("shape (kích thước):", a.shape)
print("len (độ dài):", len(a))
print("itemsize (kích thước của mỗi phần tử):", a.itemsize)
print("dtype (kiểu dữ liệu):", a.dtype)
print()

print("Mảng b:")
print(b)
print("ndim (số chiều):", b.ndim)
print("shape (kích thước):", b.shape)
print("len (độ dài):", len(b))
print("itemsize (kích thước của mỗi phần tử):", b.itemsize)
print("dtype (kiểu dữ liệu):", b.dtype)
print()

print("Ma trận c:")
print(c)
print("ndim (số chiều):", c.ndim)
print("shape (kích thước):", c.shape)
print("len (độ dài):", len(c))
print("itemsize (kích thước của mỗi phần tử):", c.itemsize)
print("dtype (kiểu dữ liệu):", c.dtype)
print()

print("Ma trận đơn vị d:")
print(d)
print("ndim (số chiều):", d.ndim)
print("shape (kích thước):", d.shape)
print("len (độ dài):", len(d))
print("itemsize (kích thước của mỗi phần tử):", d.itemsize)
print("dtype (kiểu dữ liệu):", d.dtype)
print()

print("Ma trận đường chéo e:")
print(e)
print("ndim (số chiều):", e.ndim)
print("shape (kích thước):", e.shape)
print("len (độ dài):", len(e))
print("itemsize (kích thước của mỗi phần tử):", e.itemsize)
print("dtype (kiểu dữ liệu):", e.dtype)