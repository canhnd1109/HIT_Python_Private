# Tạo từ điển với các khóa là Mã sinh viên và các giá trị là Điểm tổng kết của sinh viên
student_scores = {
    "SV001": 2.8,
    "SV002": 3.2,
    "SV003": 2.1,
    "SV004": 3.5,
    "SV005": 1.9
}

# Đếm số sinh viên có điểm tổng kết trong đoạn [2.5, 3.5]
count_students = 0
for score in student_scores.values():
    if 2.5 <= score <= 3.5:
        count_students += 1

print("Số sinh viên có điểm tổng kết trong đoạn [2.5, 3.5]:", count_students)

# Bổ sung thêm một sinh viên vào từ điển
student_scores["SV006"] = 2.7

# Xóa sinh viên có điểm tổng kết nhỏ hơn 2.0 ra khỏi từ điển
keys_to_remove = []
for key, value in student_scores.items():
    if value < 2.0:
        keys_to_remove.append(key)

for key in keys_to_remove:
    del student_scores[key]

# In toàn bộ từ điển ra màn hình
print("Từ điển sau khi xóa sinh viên có điểm tổng kết nhỏ hơn 2.0:")
for key, value in student_scores.items():
    print(key, ":", value)