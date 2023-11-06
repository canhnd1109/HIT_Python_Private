my_list = [1, 2, 3]
my_list1 = [1, 2, 3]

print ("my-list == my_list1",my_list==my_list1)
print("my_list is my_list1", my_list is my_list1)

a = ["eat","sleep", "repeat"]
for idex, val in enumerate(a):
    print(idex, val)

for i, (x, y, z) in enumerate(zip(my_list, my_list1,a)):
    print(i, " ", x, " ", y, " ", z, " ")