import numpy as np

# Lập 1 mảng 2 chiều lưu lần lượt điểm đại số tuyến tính, xác suất thống kê, giải tích với 20 phần tử mỗi hàng random trong khoảng từ [0, 10]
scores = np.random.randint(0, 11, (3, 20))
print("Mảng điểm:")
print(scores)
print()

# In ra giá trị điểm lớn nhất và nhỏ nhất ở mỗi môn
max_scores = np.max(scores, axis=1)
min_scores = np.min(scores, axis=1)

print("Điểm lớn nhất của mỗi môn:")
print(max_scores)
print()

print("Điểm nhỏ nhất của mỗi môn:")
print(min_scores)
print()

# Làm phẳng mảng và xóa đi các vị trí có điểm là 0
flatten_scores = scores.flatten()
nonzero_scores = flatten_scores[flatten_scores != 0]

print("Mảng sau khi làm phẳng và xóa các điểm bằng 0:")
print(nonzero_scores)
print()

# Sắp xếp giảm theo thuật toán quicksort
sorted_scores = np.sort(nonzero_scores)[::-1]

print("Mảng sau khi sắp xếp giảm dần:")
print(sorted_scores)
print()

# Nhập vào một số thực k từ bàn phím và cho biết vị trí chèn k vào mảng mà không phá vỡ tính sắp xếp của mảng và thêm vào vị trí đó
k = float(input("Nhập số thực k: "))
insert_index = np.searchsorted(sorted_scores, k)

print("Vị trí chèn k vào mảng là:", insert_index)
sorted_scores = np.insert(sorted_scores, insert_index, k)

print("Mảng sau khi chèn k vào vị trí đó:")
print(sorted_scores)