def input_arr(n:int) -> list:
    arr = []
    for i in range(n):
        n = int(input("Nhập phần tử thứ {}:".format(i+1)))
        arr.append(n)
    return arr

def sum(arr, x:int):
    if x<0 or x>len(arr):
        return None
    
    sum = 0
    for i in range(x+1):
        sum+=arr[i]
    return sum

n  =int(input("Nhập số phần tử của mảng đê: "))
arr = input_arr(n)
x = int(input("Nhập giá trị của x đê: "))

sum_to_x = sum(arr, x)
if sum_to_x is not None:
    print("Tổng từ vị trí đầu đến x là:", sum_to_x)
else:
    print("Giá trị x không hợp lệ.")


