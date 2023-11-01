# Nhập chuỗi ký tự từ người dùng
chuoi = input("Nhập vào một chuỗi ký tự: ")

# Kiểm tra chuỗi có chứa "hit" hoặc "HIT" hay không
co_hit = "hit" in chuoi.lower()
print(co_hit)

# Kiểm tra chuỗi có chứa số 14 hay không
co_so_14 = "14" in chuoi
print(not co_so_14)
