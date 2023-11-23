championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Tryndamere"]
dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}	
]

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
# x = zip(a, b)

# Xây dựng từ điển dựa trên hai danh sách
champion_dict = {}
for champion, data in zip(championLOL, dataLOL):
    champion_dict[champion] = data

# Kiểm tra và in giá của champion s
s = input("Nhập tên champion: ")
if s in champion_dict:
    price = champion_dict[s]["price"]
    print("Giá của champion", s, "là:", price)
else:
    print("Không tồn tại champion", s)