import math
class PTBac2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    #Xay dung phuong thuc tinh delta
    def tinhDelta(self):
        delta = self.b * self.b - 4 * self.a * self.c
        return delta
    #Xay dung phuong thuc tinh nghiem
    def tinhNghiem(self, delta):
        if(delta < 0):
            print("Phuong trinh vo nghiem")
        else:
            x1 = round((-self.b - math.sqrt(delta)) / (2 * self.a),2)
            x2 = round((-self.b + math.sqrt(delta)) / (2 * self.a),2)
            print("Nghiem x1 =", x1, "va nghiem x2 =",x2)
# Ham nhap phuong trinh bac 2
def nhapPT():
    a = float(input("Nhap he so a = "))
    b = float(input("Nhap he so b = "))
    c = float(input("Nhap he so c = "))
    pt1 = PTBac2(a, b, c)
    return pt1
# Ham luu he so a, b, c vao file
def luuVaoFile(pt1):
    with open("ptb2.txt", "w") as file:
        file.write(str(pt1.a) + "\n")
        file.write(str(pt1.b) + "\n") 
        file.write(str(pt1.c) + "\n")
    print("Ban da ghi a, b, c vao file")
# Ham doc he so a, b, c tu file
def docTuFile():
    with open("ptb2.txt","r") as file:
        a = float(file.readline())
        b = float(file.readline())
        c = float(file.readline())
        pt1 = PTBac2(a, b, c)
        print("Ban da doc du lieu tu file thanh cong")
    return pt1
# Ham main
def main():
    while True:
        print("He thong lua chon:")
        print("1. Nhap he so a, b, c cua phuong trinh")
        print("2. Doc a, b, c tu file")
        print("3. Tinh nghiem")
        print("4. Luu he so a, b, c vao file va thoat")
        luaChon = int(input("Moi ban lua chon thuc don (1 - 4): "))
        if(luaChon == 1):
            pt1 = nhapPT()
            input()
        elif(luaChon == 2):
            pt1 = docTuFile()
            input()
        elif(luaChon == 3):
            delta = pt1.tinhDelta()
            pt1.tinhNghiem(delta)
            input()
        elif(luaChon == 4):
            luuVaoFile(pt1)
            break

main()

