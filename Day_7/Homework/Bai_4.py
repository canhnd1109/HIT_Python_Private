class Hiter:
    id = 2022605692
    danhSachHiter = []
    
    def __init__(self, ten, tuoi, gen):
        self.id = Hiter.id
        self.ten = ten
        self.tuoi = tuoi
        self.gen = gen 
        Hiter.id += 1
        Hiter.danhSachHiter.append(self)
    
    def nhap(self):
        self.ten = input("Nhap ten: ")
        self.tuoi = input("Nhap tuoi: ")
        self.gen = input("Nhap gioi tinh: ")
        
        Hiter.danhSachHiter.append(self)
    
    def __str__(self):
        return f"{self.id} \t {self.ten} \t {self.tuoi} \t {self.gen}"
    
    @staticmethod
    def danhSach():
        for i in Hiter.danhSachHiter:
            print(i)
    
class Ban:
    def __init__ (self, idBan=None, tenBan=None, truongban:Hiter=None, thanhVien:list=None):
        self.idBan = idBan
        self.tenBan = tenBan
        self.truongBan = truongban
        self.thanhVien = thanhVien
    
    def nhap(self):
        self.idBan = input("Nhap id ban: ")
        self.tenBan = input("Nhap ten ban: ")

        print("Nhap thong tin truong ban: ")
        self.truongBan = Hiter("", 0, "")
        self.truongBan.nhap()
        
        print("nhap thong tin thanh vien: ")
        for nguoi in range(int(input("Nhap so thanh vien: "))):
            print(f"Nhap thong tin thanh vien {nguoi + 1}: ")
            nguoi = Hiter("", 0, "")
            nguoi.nhap()
            self.thanhVien.append(nguoi)
            
    def __str__(self):
        return f"idBan={self.idBan}, tenBan={self.tenBan} \nTrưởng ban: {self.truongBan}\n" + '\n'.join([f"Thành viên {i+1}: {self.thanhVien[i]}" for i in range(len(self.thanhVien))])
    
    def dsHiter(self):
        for i in self.thanhVien:
            print(i)

    def xoa(self, id:str):
        for hiter in self.thanhVien:
            if hiter.id == id:
                self.thanhVien.remove(hiter)
                print(f"Da xoa Hiter {id} khoi ban {self.tenBan}")
                break
            else:
                print(f"Khong tim thay Hiter {id} trong ban {self.tenBan}")
    
    def add(self):
        ten = input("Nhap ten Hiter can them: ")
        tuoi = int(input("Nhap tuoi Hiter can them: "))
        gen = input("Nhap gioi tinh Hiter can them: ")
        
        for hiter in self.thanhVien:
            if hiter.ten == ten and hiter.tuoi == tuoi and hiter.gen == gen:
                print("Hiter da co trong ban!")
                return

        for hiter in Hiter.danhSachHiter:
            if hiter.ten == ten and hiter.tuoi == tuoi and hiter.gen == gen:
                self.thanhVien.append(hiter)
                print("Thêm thành công")

if __name__ == '__main__':
    h1 = Hiter("Huy", 20, "Nam")
    h2 = Hiter("Hoa", 20, "Nu")
    h3 = Hiter("Hien", 20, "Nu")
    h4 = Hiter("Huong", 20, "Nu")
    h5 = Hiter("Hai", 20, "Nam")
    h6 = Hiter("hai", 20, "Nam")
    h7 = Hiter("hoang", 20, "Nu")
    h8 = Hiter("hung hun", 20, "Nu")
    h9 = Hiter("giang", 20, "Nam")
    h10 = Hiter("hoa", 20, "Nam")
    
    Hiter.danhSach()    
    
    print("\nDanh sach ban: ")
    khmt = Ban("2022605692", "Mỹ thuật đại cương", h1, [h1, h2, h3, h4, h5])
    print(khmt)
    
    print("\nDanh sach ban: ")
    ktmp = Ban("2022605692", "Mỹ thuật", h6, [h6, h7, h8, h9, h10])
    print(ktmp)
    