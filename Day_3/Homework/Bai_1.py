
#Su dung ham map() va float de ep kieu du lieu sang so thuc
x1, y1, x2, y2, x3, y3 = map(float, input().split())

#Dung cau lenh re nhanh de kiem tra dieu kien
if x1+1==y1 and y1+1==x2 and x2+1==y2 and y2+1==x3 and x3+1==y3:
   #Neu dieu kien dung thi xuat thong bao
   print("{}, {}, {},{}, {}, {},khong la toa do cua mot tam giac".format(x1, y1, x2, y2, x3, y3))
else:
   #Neu dieu kien sai thi xuat thong bao
   print("{}, {}, {},{}, {}, {}, la toa do cua mot tam giac".format(x1, y1, x2, y2, x3, y3))


    