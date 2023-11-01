a = 10
bit_count = a.bit_length()

print("Số lượng bit cần thiết:", bit_count)

attributes = dir(a)

print("Danh sách thuộc tính và phương thức của biến 'a':")
for attr in attributes:
    print(attr)