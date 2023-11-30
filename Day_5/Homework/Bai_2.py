# # USE CHATGPT em đọc không hiểu gì. Hiccc

# # Nhập dữ liệu từ người dùng
# n = int(input("Nhập số phần tử của set: "))
# input_set = set()
# for _ in range(n):
#     element = int(input("Nhập phần tử: "))
#     input_set.add(element)

# target_sum = int(input("Nhập tổng cần đạt được: "))


# def find_largest_subset(input_set, target_sum):
#     # Chuyển đổi set thành list để dễ xử lý
#     elements = list(input_set)
#     n = len(elements)

#     # Khởi tạo mảng 2D để lưu trữ thông tin về tập con có tổng lớn nhất
#     dp = [[0] * (target_sum + 1) for _ in range(n + 1)]

#     # Xây dựng bảng dp
#     for i in range(1, n + 1):
#         for j in range(target_sum + 1):
#             # Nếu phần tử hiện tại lớn hơn tổng cần đạt được, bỏ qua nó
#             if elements[i - 1] > j:
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 # So sánh giữa việc bỏ qua phần tử và bao gồm nó
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - elements[i - 1]] + elements[i - 1])

#     # Truy vết để xác định tập hợp con lớn nhất
#     result_set = set()
#     i, j = n, target_sum
#     while i > 0 and j > 0:
#         if dp[i][j] != dp[i - 1][j]:
#             result_set.add(elements[i - 1])
#             j -= elements[i - 1]
#         i -= 1

#     return result_set

# # Gọi hàm và in kết quả
# result = find_largest_subset(input_set, target_sum)
# print("Tập hợp con lớn nhất có tổng không vượt quá", target_sum, "là:", result)



n = int(input("Nhập số lượng phần tử của set: "))
s = set(map(int,input().split()))
a = int(input("Nhập a: "))

subset = set()
current_sum = 0

for i in s:
    if current_sum + i <= a:
        subset.add(i)
        current_sum += i
    else:
        break

print(subset)