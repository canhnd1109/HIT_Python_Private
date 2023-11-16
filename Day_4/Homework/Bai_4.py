N = int(input("Nhập số lượng phần tử trong mảng: "))
array = list(map(int, input("Nhập các số trong mảng (cách nhau bởi dấu cách): ").split()))

# Tính tổng số chẵn và tổng số lẻ
sum_even = 0
sum_odd = 0
for num in array:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

# So sánh tổng và in kết quả
if sum_even > sum_odd:
    print("even")
elif sum_even < sum_odd:
    print("odd")
else:
    print("equal")