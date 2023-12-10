class Pycon:
    id = 1
    def __init__(self, name, age):
        self.id = Pycon.id
        Pycon.id += 1
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Pycon {self.id}: {self.name}, {self.age} tuổi"
    
    @classmethod
    def average_age(cls, pycons):
        sum = 0
        for p in pycons:
            sum +=p.age

        return sum/len(pycons)


n = int(input("Nhập số lượng Pycon: "))

pycons =[]

for i in range(n):
    print(f"\nNhập thông tin Pycon thứ {i+1}:")
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    pycon = Pycon(name, age)
    pycons.append(pycon)
    print(pycon)

tuoi_tb = Pycon.average_age(pycons)
print("\nTrung bình độ tuổi của các Pycon là:", tuoi_tb)