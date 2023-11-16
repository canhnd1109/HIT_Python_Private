input_list = input("Nhập danh sách các giá trị (cách nhau bởi dấu cách): ").split()

grouped_dict = {}
for value in input_list:
    if value in grouped_dict:
        grouped_dict[value].append(value)
    else:
        grouped_dict[value] = [value]

grouped_list = list(grouped_dict.values())
print(grouped_list)