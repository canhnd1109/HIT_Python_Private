import re

str = input("Nhập chuỗi số: ")

list = re.findall(r'-?\d+', str)   
 # \d+ <=> \d{1,} : tìm những số có từ 1 chữ số 
total = 0
for number in list:
    total+=int(number)

print("Tổng các số trong chuỗi là:", total)
