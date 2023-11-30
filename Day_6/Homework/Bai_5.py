def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(n, m):
    x = gcd(n, m)
    t = n // x
    m = m // x
    return t, m

def tich(n):
    tu_so = 1
    mau_so = 1

    for _ in range(n):
        t = int(input("Nhập tử số: "))
        m = int(input("Nhập mẫu số: "))

        # Nhân tử số
        tu_so *= t

        # Nhân mẫu số
        mau_so *= m

    # Rút gọn phân số tích
    tu_short, mau_short = rut_gon(tu_so, mau_so)

    return tu_short, mau_short

n = int(input("Nhập số phân số: "))
tu_short, mau_short = tich(n)
print("Tích của các phân số là: {}/{}".format(tu_short, mau_short))


