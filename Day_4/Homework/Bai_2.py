N = int(input("Nhập số lượng số Nasus có: "))
numbers = list(map(int, input("Nhập các số Nasus có (cách nhau bởi dấu cách): ").split()))

# Xác định các số thầy Ba thích
teacher_Ba_like = []
for num in numbers:
    if num % 10 in [1, 3, 5, 7, 9]:
        teacher_Ba_like.append(num)

# Sắp xếp các số thầy Ba thích theo thứ tự tăng dần
teacher_Ba_like.sort()

# In kết quả
print("Số lượng số thầy Ba thích trong các số Nasus có:", len(teacher_Ba_like))
print("Các số thầy Ba thích theo thứ tự tăng dần:", ' '.join(map(str, teacher_Ba_like)))


