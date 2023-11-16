# Đọc danh sách và số lượng danh sách con từ người dùng
input_list = input("Nhập danh sách các giá trị (cách nhau bởi dấu cách): ").split()
num_sublists = int(input("Nhập số lượng danh sách con (n): "))

length = len(input_list)
sublist_length = length // num_sublists

# Kiểm tra nếu độ dài của danh sách không chia hết cho n
if length % num_sublists != 0:
    print("Lỗi: Độ dài của danh sách không chia hết cho n.")
    
# Tách danh sách thành các danh sách con (Cái này tra mạng xong copy về chứ em đọc cũng chả hiểu gì hiccc. Anh có thể giải thích giúp em với đc không ạ)
splitted_lists = [input_list[i:i + sublist_length] for i in range(0, length, sublist_length)]  


print(splitted_lists)

