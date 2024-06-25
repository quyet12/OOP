def nhapDaThuc():
    daThuc = {}

    while(True):
        mu = int(input("Nhap mu = "))
        if(mu == -1):
            break
        heSo = float(input("Nhap he so = "))
        if(heSo != 0):
            daThuc[mu] = heSo

    return daThuc

def hienThiDT(daThuc):
    chuoiDaThuc = ""
    for mu in sorted(daThuc.keys()):
        if(daThuc[mu] > 0):
            chuoiDaThuc = chuoiDaThuc + "+" + str(daThuc[mu]) + "* x^" + str(mu)
        else:
            chuoiDaThuc = chuoiDaThuc + str(daThuc[mu]) + "* x^" + str(mu)
    print("P = ", chuoiDaThuc)

def tongDT(daThuc1, daThuc2):
    daThucTong = {}
    # Xet mu co trong da thuc 1
    for mu in daThuc1:
        if(mu in daThuc2):
            daThucTong[mu] = daThuc1[mu] + daThuc2[mu]
        else:
            daThucTong[mu] = daThuc1[mu]
    # Xet mu co trong da thuc 2
    for mu in daThuc2:
        if(mu not in daThuc1):
            daThucTong[mu] = daThuc2[mu]

    return daThucTong

def tinhGTDT(daThuc, x):
    return sum(daThuc[mu] * (x ** mu) for mu in daThuc)

def main():
    print("Nhap da thuc 1")
    daThuc1 = nhapDaThuc()
    print("Nhap da thuc 2")
    daThuc2 = nhapDaThuc()
    
    print("Tong 2 da thuc:")
    daThucTong = tongDT(daThuc1, daThuc2)
    hienThiDT(daThuc1)
    hienThiDT(daThuc2)
    hienThiDT(daThucTong)

    x = int(input("Nhap vao x = "))
    print("Gia tri cua da thuc 1 tai x =", x, "la:" , tinhGTDT(daThuc1, x))

main()

