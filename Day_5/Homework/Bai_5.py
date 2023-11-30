lucky_number = 11

# Nhập set từ bàn phím
set_numbers = set(input("Nhập các số vào set, cách nhau bằng dấu cách: ").split())

# Kiểm tra và thêm số 11 vào set nếu chưa tồn tại
if str(lucky_number) not in set_numbers:
    set_numbers.add(str(lucky_number))

print("Các số trong set:")
print(set_numbers)

# Tìm cặp số có tổng bằng con số may mắn
number_pairs = []
for num1 in set_numbers:
    for num2 in set_numbers:
        if num1 != num2:
            if int(num1) + int(num2) == lucky_number:
                number_pairs.append((int(num1), int(num2)))

print("Các cặp số có tổng bằng", lucky_number, ":")
for pair in number_pairs:
    print(pair)

# Kết hợp các cặp số thành một tuple và tính tổng của nó
combined_tuple = tuple(number_pairs)
total_sum = sum(sum(pair) for pair in combined_tuple)

print("Tổng của các số trong tuple:", total_sum)