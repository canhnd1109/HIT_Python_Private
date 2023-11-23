# Nhập chuỗi từ bàn phím
input_string = input("Nhập chuỗi: ")


char_count = 0
# Tạo từ điển với key là các kí tự trong chuỗi và value là số lần xuất hiện
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


# In từ điển ra màn hình
print("Từ điển:")
for key, value in char_count.items():
    print(key, ":", value)


























