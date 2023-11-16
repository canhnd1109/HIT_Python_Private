n = int(input("Nhập số nguyên dương n (2 <= n <=100): "))
m = int(input("Nhập số nguyên dương m (m >= 3): "))

# Kiểm tra giá trị của n và m
if n < 2 or n > 100 or m < 3:
    print("Gia tri khong hop le.")
    exit()

for i in range(n): 
    # Nhập n số nguyên dương có từ 6 chữ số trở lên
    s = input("nhập vào một số nguyên dương có từ 6 chữ số trở nên: "); 
     # Đảo chiều m số cuối cùng của từng số nguyên và in ra kết quả
    print(s[:-m] + s[:m - 1:-1])
    print(s[:m] + s[:m - 1:-1])