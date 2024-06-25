class BaiHat:
    def __init__(self, tieuDe, url):
        self.tieuDe = tieuDe
        self.url = url

class PlayList:
    def __init__(self, tenPlayList, moTa, danhGia, dsBaiHat):
        self.tenPlayList = tenPlayList
        self.moTa = moTa
        self.danhGia = danhGia
        self.dsBaiHat = dsBaiHat

# Ham nhap mot bai hat
def nhapBaiHat():
    tieuDe = input("Nhap tieu de bai hat: ") + "\n"
    url = input("Nhap url bai hat: ") + "\n"
    baiHat = BaiHat(tieuDe, url)
    return baiHat

# Ham nhap danh sach bai hat
def nhapDSBaiHat():
    n = int(input("Nhap so luong bai hat: "))
    dsBaiHat = []
    for i in range(n):
        print("Nhap bai hat", i + 1,":")
        baiHat = nhapBaiHat()
        dsBaiHat.append(baiHat)
    return dsBaiHat

# Nhap Playlist
def nhapPlayList():
    tenPlayList = input("Nhap vao ten Playlist: ") + "\n"
    moTa = input("Mo ta Playlist: ") + "\n"
    danhGia = input("Danh gia PlayList (nhap tu 1 den 5 sao): ") + "\n"
    dsBaiHat = nhapDSBaiHat()
    playList = PlayList(tenPlayList, moTa, danhGia, dsBaiHat)
    return playList

# Ham ghi mot bai hat vao file
def ghiBaiHatVaoFile(baiHat, file):
    file.write(baiHat.tieuDe)
    file.write(baiHat.url)

# Ham ghi danh sach bai hat vao file
def ghiDSBaiHatVaoFile(dsBaiHat, file):
    n = len(dsBaiHat)
    file.write(str(n) + "\n")
    for i in range(n):
        ghiBaiHatVaoFile(dsBaiHat[i], file)

# Ghi playlist vao file
def ghiPlayListVaoFile(playList):
    with open("BaiHat.txt", "w") as file:
        file.write(playList.tenPlayList)
        file.write(playList.moTa)
        file.write(playList.danhGia)
        ghiDSBaiHatVaoFile(playList.dsBaiHat, file)

# Doc mot bai hat tu file
def docBaiHatTuFile(file):
    tieuDe = file.readline()
    url = file.readline()
    baiHat = BaiHat(tieuDe, url)
    return baiHat

# Doc danh sach bai hat tu file
def docDSBaiHatTuFile(file):
    dsBaiHat = []
    n = int(file.readline())
    for i in range(n):
        baiHat = docBaiHatTuFile(file)
        dsBaiHat.append(baiHat)
    return dsBaiHat

# Doc playlist tu file
def docPlayListTuFile():
    with open("Baihat.txt", "r") as file:
        tenPlayList = file.readline()
        moTa = file.readline()
        danhGia = file.readline()
        dsBaiHat = docDSBaiHatTuFile(file)
        playList = PlayList(tenPlayList, moTa, danhGia, dsBaiHat)
    return playList

# In thong tin mot bai hat ra man hinh
def inBaiHat(baiHat):
    print("Tieu de cua bai hat la: ", baiHat.tieuDe, end = "")
    print("URL cua bai hat la: ", baiHat.url, end = "")

# In thong tin danh sach bai hat ra man hinh
def inDSBaiHat(dsBaiHat):
    print("\nThong tin tin cac bai hat:")
    for i in range(len(dsBaiHat)):
        inBaiHat(dsBaiHat[i])

# In thong tin playlist ra man hinh
def inPlayList(playList):
    print("Ten playlist la:", playList.tenPlayList, end = "")
    print("Mo ta playlist:", playList.moTa, end = "")
    print("Danh gia playlist:", playList.danhGia, end = "")
    print("Danh sach bai hat trong playlist:", end = "")
    inDSBaiHat(playList.dsBaiHat)

def main():
    # baiHat = nhapBaiHat()
    # ghiBaiHatVaoFile(baiHat)
    # baiHat = docBaiHatTuFile()
    # inBaiHat(baiHat)

    # dsBaiHat = nhapDSBaiHat()
    # ghiDSBaiHatVaoFile(dsBaiHat)
    # dsBaiHat = docDSBaiHatTuFile()
    # inDSBaiHat(dsBaiHat)

    # playList = nhapPlayList()
    # ghiPlayListVaoFile(playList)
    playList = docPlayListTuFile()
    inPlayList(playList)

main()
