from datetime import datetime

# Nhập chuỗi ngày từ người dùng
date_string = input("Nhập chuỗi ngày (dd/mm/yyyy): ")
d, m , y = list(map(int, date_string.split('/')))
if 31<d<1 and 12<m<1 and y<1000: 
    print("Invalid ") 
else:
   # Chuyển đổi chuỗi ngày thành đối tượng datetime
   date = datetime.strptime(date_string, "%d/%m/%Y")
   # Tính toán ngày cuối năm
   the_last_day = datetime(date.year, 12, 31)
   # Đếm số ngày từ ngày nhập vào đến cuối năm
   days_count = (the_last_day - date).days

print("Số ngày từ ngày nhập vào đến cuối năm là:", days_count)