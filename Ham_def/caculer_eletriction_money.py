def tinhTienDien(kw):
    tienDien = 0
    vat = 0
    tongTien = 0
    if (kw <= 100):
        tienDien = kw * 1500
    elif(101 <= kw <= 200):
        tienDien = 100 * 1500 + (kw - 100) * 2000
    elif(201 <= kw <= 300):
        tienDien = 100 * 1500 + 100 * 2000 + (kw - 200) * 2500
    else:
        tienDien = 100 * 1500 + 100 * 2000 + 100 * 2500 + (kw - 300) * 3000
    vat = tienDien * 0.1
    tongTien = tienDien + vat
    return int(tongTien)
    

def main():
    n = int(input("Nhap vao so luong ho: "))

    for i in range(n):
        maHo = ""
        tenHo = ""
        diaChi = ""
        kw = 0
        while True:
            maHo = input("Nhap vao ma ho: ") + "\n"
            if(maHo != ""):
                break
        while True:
            tenHo = input("Nhap vao ten chu ho: ") + "\n"
            if(tenHo != ""):
                break
        while True:
            diaChi = input("Nhap vao dia chi: ") + "\n"
            if(diaChi != ""):
                break
        while True:
            kw = int(input("Nhap vao so KW tieu thu: "))
            if(kw >= 0):
                break
        
        tongTien = tinhTienDien(kw)
        kw = str(kw) + "\n"
        tongTien = str(tongTien) + "\n"

        with open("Data.txt", "a") as file:
            file.writelines([maHo, tenHo, diaChi, kw, tongTien])
    print("\t".join(["Ma ho", "Ten ho", "Dia chi", "So KW", "Tong tien dien"]))
    cnt = 0
    with open("Data.txt", "r") as file:
        for ho in file.readlines():
            print(ho.replace("\n","") + "\t", end = "")
            cnt += 1
            if(cnt % 5 == 0):
                print()

main()