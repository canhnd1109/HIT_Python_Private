# class mynumber:
#     def __init__(self, value):
#         self.value = value
     
#     def print_value(self):
#         print(self.value)
 
# obj1 = mynumber(17)
# obj1.print_value()

# class Nguoi():
#     name= "canh"
#     def __init__(self, name) -> None:
#         self.name=name

#     @classmethod
#     def ngu(self):
#         print(self.name,"kho"*2)

    

# Canh = Nguoi("abc")

# Canh.ngu()
# Nguoi.ngu()


class PhanSo:
    def __init__(self, a, b):
        self.tuSo = a
        self.mauSo = b
    def __add__(self, other):
        self.tuSo = self.tuSo * other.mauSo + self.mauSo * other.tuSo
        self.mauSo = self.mauSo*self.mauSo
        return str(self.tuSo) + "/"+str(self.mauSo)
ps1 = PhanSo(1, 2)
ps2 = PhanSo(3, 4)
print(ps1 + ps2)