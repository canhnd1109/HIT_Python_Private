import random
# Nhập số lượng tài khoản sinh viên
N = int(input("Nhập số lượng tài khoản sinh viên (10 <= N < 100000): "))

# Tạo danh sách các chuyên ngành
majors = ["CNTT", "KHMT", "KTPM", "HTTT"]

# Hàm tạo mật khẩu ngẫu nhiên
def generate_password(major, student_id):
    return major + student_id

# Tạo từ điển chứa thông tin tài khoản của sinh viên
accounts = {}
for i in range(N):
    student_id = str(2021600000 + i + 1)
    username = student_id
    password = generate_password(random.choice(majors), student_id)
    account_name = "Account" + str(i + 1)
    account_info = {
        "Username": username,
        "Password": password
    }
    accounts[account_name] = account_info

# In thông tin tài khoản của sinh viên
for account, info in accounts.items():
    print(account + ":")
    print("Username:", info["Username"])
    print("Password:", info["Password"])