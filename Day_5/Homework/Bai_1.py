table_1 = set(input("Nhập danh sách mã sinh viên ở bàn 1 (cách nhau bằng dấu cách): ").split())
table_2 = set(input("Nhập danh sách mã sinh viên ở bàn 2 (cách nhau bằng dấu cách): ").split())


# intersection() trả về một tập hợp chứa sự giống nhau giữa hai hoặc nhiều tập hợp.
# Tìm sinh viên đăng ký ở cả hai bàn
register_2_table = table_1.intersection(table_2)
# In danh sách sinh viên đăng ký ở cả hai bàn
if register_2_table >0:
    print("Sinh viên đăng ký ở cả hai bàn:", register_2_table)


#union() Trả về một bộ chứa tất cả các mục từ cả hai bộ, loại trừ các mục trùng lặp:
# Tổng hợp danh sách sinh viên đã đăng ký của cả hai bàn
registration_summary = table_1.union(table_2)
# In danh sách tổng hợp sinh viên đã đăng ký của cả hai bàn
print("Tổng hợp sinh viên đã đăng ký của cả hai bàn:", registration_summary)

# Sinh viên đăng ký tại bàn 1 nhưng không đăng ký tại bàn 2
register_table_1_not_table_2 = table_1.difference(table_2)
# In danh sách sinh viên đăng ký tại bàn 1 nhưng không đăng ký tại bàn 2
print("Sinh viên đăng ký tại bàn 1 nhưng không đăng ký tại bàn 2:", register_table_1_not_table_2)

# Sinh viên đăng ký duy nhất ở một bàn
register_only_one_table_1 = table_1.difference(table_2)
register_only_one_table_2 = table_2.difference(table_2)
register_only_one_table = register_only_one_table_1.union(register_only_one_table_2)

# In danh sách sinh viên đăng ký duy nhất ở một bàn
print("Sinh viên đăng ký duy nhất ở một bàn:", register_only_one_table)
