k = int(input("Nhập vào một số học sinh k: "))

for i in range(1, k+1):
    name = input("Nhập Tên: ")
    tx1 = int(input("Nhập điêmt thường xuyên 1: "))
    tx2 = int(input("Nhập điêmt thường xuyên 2: "))
    sum = tx1 + tx2
    if (sum >= 190):
       result =  "Xuất sắc"
       print(name, sum, result)
    elif( 150<=sum<190):
       result = "Giỏi"
       print(name, sum, result)
    elif( 100<= sum <150):
      result =  "Khá"
      print(name, sum, result)
    else:
       result = "Yếu"
       print(name, sum, result)