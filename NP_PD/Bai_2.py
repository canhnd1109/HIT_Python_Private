import numpy as np

# Nhập từ bàn phím 2 vector numpy a, b có cùng kích thước n
n = int(input("Nhập kích thước n: "))
a = np.random.rand(n)
b = np.random.rand(n)

# In ra max, min, giá trị trung bình, độ lệch chuẩn của vector, giá trị trung vị
print("Vector a:")
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Giá trị trung bình:", np.mean(a))
print("Độ lệch chuẩn:", np.std(a))
print("Giá trị trung vị:", np.median(a))
print()

print("Vector b:")
print("Max:", np.max(b))
print("Min:", np.min(b))
print("Giá trị trung bình:", np.mean(b))
print("Độ lệch chuẩn:", np.std(b))
print("Giá trị trung vị:", np.median(b))
print()

# Tạo ma trận numpy c (2-D) có kích thước nx2 từ a, b
c = np.column_stack((a, b))
print("Ma trận c:")
print(c)
print()

# Khởi tạo ma trận (2-D) numpy d với kích thước nxn theo phân phối Gauss (với mean, std của b)
mean_b = np.mean(b)
std_b = np.std(b)
d = np.random.normal(mean_b, std_b, (n, n))
print("Ma trận d:")
print(d)
print()

# Tính tổng, hiệu, tích 2 ma trận
sum_ab = a + b
diff_ab = a - b
prod_ab = np.dot(a, b)

# Tính tích ma trận chuyển vị của d với ma trận nghịch đảo của d
d_inv = np.linalg.inv(d)
prod_d_inv = np.dot(d.T, d_inv)

print("Tổng của a và b:")
print(sum_ab)
print()

print("Hiệu của a và b:")
print(diff_ab)
print()

print("Tích của a và b:")
print(prod_ab)
print()

print("Tích của d và ma trận nghịch đảo của d:")
print(prod_d_inv)
print()

# Chuyển ma trận c về tensor numpy e (3-D)
e = np.expand_dims(c, axis=0)
print("Tensor e:")
print(e)