
# print('\u00D2')   
# # y+x


# # keu ra tieng pip khi run tren terminal
# print('\a')

# print("Ngo Duc \b Canh")
# print("Ngo Duc \n Canh")
# print("Ngo Duc \t Canh")
# print("Ngo Duc \' Canh")


# s= r"D:\HIT\btvn"

# print(s)

# s1 = "|{:<10}|{:^10}|{:>10}|".format("list", 'tuple', 'set')
# print(s1)


# s2 = "HIT Python"

# for letter in s2:
#     print(letter)


# for i in range(len(s2)):
#     print(s2[i])


# a = 'abcdEFGH'
# print(a.strip())
# print(a.split())



input_string = input("Nhập một chuỗi: ")

# Tách chuỗi thành các từ
words = input_string.split()

# Đếm số từ trong chuỗi
word_count = len(words)

# In số từ ra màn hình
print("Số từ trong chuỗi là:", word_count)