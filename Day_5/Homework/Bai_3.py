
text = input("Enter the text: ").split()
char_count = 0

char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Số thứ tự xuất hiện của các từ: ")
for key, value in char_count.items():
    print(key, ":", value)

