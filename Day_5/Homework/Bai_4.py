
def is_number(string):
    # Hàm kiểm tra xem một chuỗi có phải là dạng số hay không
    return string.isdigit()

n = int(input("Nhập số phần tử của mảng a: "))

a = []
for i in range(n):
    element = input("Nhập phần tử thứ {} của mảng a: ".format(i + 1))
    a.append(element)

b = tuple(a)

# In các phần tử của tuple b
print("Các phần tử của tuple b:")
for element in b:
    print(element)

# Đếm số phần tử trong b có dạng số
count = 0
for element in b:
    if is_number(element):
        count += 1

print("Số phần tử trong b có dạng số: ", count)