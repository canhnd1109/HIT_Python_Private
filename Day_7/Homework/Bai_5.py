import math

class PhanSo:
    def __init__(self, __tu_so, __mau_so):
        if __mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0.")
        ucln = math.gcd(__tu_so, __mau_so)
        self.__tu_so = __tu_so // ucln
        self.__mau_so = __mau_so // ucln
    
    def __str__(self) -> str:
        if self._PhanSo__mau_so == 1:
            return f"{self._PhanSo__tu_so}"
        return f"{self._PhanSo__tu_so}/{self._PhanSo__mau_so}"
    
    def __add__(self, other):
        tu_so = self._PhanSo__tu_so * other._PhanSo__mau_so + other._PhanSo__tu_so * self._PhanSo__mau_so
        mau_so = self._PhanSo__mau_so * other._PhanSo__mau_so
        return PhanSo(tu_so, mau_so)
    
    def __sub__(self, other):
        tu_so = self._PhanSo__tu_so * other._PhanSo__mau_so - other._PhanSo__tu_so * self._PhanSo__mau_so
        mau_so = self._PhanSo__mau_so * other._PhanSo__mau_so
        return PhanSo(tu_so, mau_so)

    def __mul__(self, other):
        tu_so = self.__tu_so * other.__tu_so
        mau_so = self.__mau_so * other.__mau_so
        return PhanSo(tu_so, mau_so)
    
    @staticmethod
    def to_honso(phanso):
        phan_nguyen = phanso.__tu_so // phanso.__mau_so
        tu_so = phanso.__tu_so % phanso.__mau_so
        mau_so = phanso.__mau_so
        return HonSo(phan_nguyen, PhanSo(tu_so, mau_so))
        
class HonSo:
    def __init__(self, __phan_nguyen, phan_so:PhanSo):
        self.__phan_nguyen = __phan_nguyen
        self.__phan_so = phan_so


    def __str__(self):
        return f"{self.__phan_nguyen}/{self.__phan_so}"

    def __add__(self, other):
        return HonSo.to_phanso(self) + HonSo.to_phanso(other)

    def __sub__(self, other):
        return HonSo.to_phanso(self) - HonSo.to_phanso(other)

    def __mul__(self, other):
        return HonSo.to_phanso(self) * HonSo.to_phanso(other)

    @staticmethod
    def to_phanso(honSo):
        tu_so = honSo._HonSo__phan_nguyen * honSo._HonSo__phan_so._PhanSo__mau_so + honSo._HonSo__phan_so._PhanSo__tu_so
        mau_so = honSo._HonSo__phan_so._PhanSo__mau_so
        return PhanSo(tu_so, mau_so) 

class Math(PhanSo, HonSo):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        if isinstance(self.a, PhanSo):
            return PhanSo.__str__(self.a)
        elif isinstance(self.a, HonSo):
            return HonSo.__str__(self.a)

    def to_honso(self):
        if isinstance(self.a, PhanSo):
            return PhanSo.to_honso(self.a)
        else:
            return self.a
    
    def to_phanso(self):
        if isinstance(self.a, HonSo):
            return HonSo.to_phanso(self.a)
        else:
            return self.a
        
    def __add__(self, other):
        if isinstance(self.a, HonSo):
            self.a = HonSo.to_phanso(self.a)
        elif isinstance(other.a, HonSo):
            other.a = HonSo.to_phanso(self.a)
       
        result = self.a + other.a
        
        return Math(result)
    
    def __sub__(self, other):
        if isinstance(self.a, HonSo):
            self.a = HonSo.to_phanso(self.a)
        elif isinstance(other.a, HonSo):
            other.a = HonSo.to_phanso(self.a)
       
        result = self.a - other.a
        
        return Math(result)
    
    def __mul__(self, other):
        if isinstance(self.a, HonSo):
            self.a = HonSo.to_phanso(self.a)
        elif isinstance(other.a, HonSo):
            other.a = HonSo.to_phanso(self.a)
       
        result = self.a * other.a
        
        return Math(result)
   
if __name__ == "__main__":
    a = Math(HonSo(4, PhanSo(1, 5)))
    b = Math(PhanSo(9, 7))
    
    print("a =", a)
    print("b =", b)
    print("a to phan so =", a.to_phanso())  
    print("b to hon so =", b.to_honso())    
    
    print("a + b =", (a + b).to_honso())
    print("b + a =", b + a)
    print("a - b =", a - b)
    print("b - a =", b - a)
    print("a * b =", a * b)
    print("b * a =", (b * a).to_honso())

