import os

danhsachloaihanghoa = []
def danhsach_loaihanghoa():
    files = os.listdir("QLBH/Data/LoaiHangHoa")
    if "loaiHangHoa.csv" not in files:
        print("Danh sach loai hang hoa khong ton tai!")
        return
    with open('../LoaiHangHoa/loaihanghoa.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_read = line.split(',')
            if len(str_to_read) > 1:
                loaihanghoa = {}
                loaihanghoa["id"] = str_to_read[0]
                tenloai = str_to_read[1]
                if tenloai.endswith('\n'):
                    tenloai = tenloai[0:len(tenloai)-1]
                loaihanghoa["ten"] = tenloai
                danhsachloaihanghoa.append(loaihanghoa)
            line = f.readline()


def xem_loaihanghoa(id=None):
    if id is None:
        id = input("Moi nhap ID loai hang hoa muon xem")
    for loaihanghoa in danhsachloaihanghoa:
        if id == loaihanghoa["id"]:
            return loaihanghoa
        else:
            print("Khong co loai hang hoa nay")
            ## Them phan bat nhap lai

def tao_loaihanghoa():
    data = {}
    id = input("Moi nhap ID loai hang hoa muon nhap: ")
    xet_id_daco = xem_loaihanghoa(id)
    if xet_id_daco is not None:
        print("Da ton tai ma loai hang nay. Xin moi nhap lai!")
        return  ## Them phan bat nhap lai

    data["id"] = id
    data["ten"] = input("Nhap ten loai hang hoa muon them: ")
    danhsachloaihanghoa.append(data)
    str_to_save = data["id"] + ',' + data["ten"] + ',' + '\n'
    with open('../LoaiHangHoa/loaihanghoa.csv', 'a') as f:
        data = f.write(str_to_save)
    print("Da them thanh cong!!!")

def sua_loaihanghoa():
    id = input("Nhap loai hang hoa muon sua: ")
    xet_id_daco = xem_loaihanghoa(id)
    if xet_id_daco is None:
        print("Loai hang hoa muon sua khong ton tai!")
        return;
    loaihanghoa = xem_loaihanghoa(id)
    loaihanghoa["id"] = id
    loaihanghoa["ten"] = input("Nhap ten loai hang hoa moi: ")
    danhsachloaihanghoa.append(loaihanghoa)
    str_to_save = loaihanghoa["id"] + ',' + loaihanghoa["ten"] + ',' + '\n'
    with open('../LoaiHangHoa/loaihanghoa.csv', 'a') as f:
        data = f.write(str_to_save)
    print("Da sua thanh cong!!!")

def xoa_loaihanghoa():
    id = input("Nhap loai hang hoa muon xoa: ")
    xet_id_daco = xem_loaihanghoa(id)
    if xet_id_daco is None:
        print("Loai hang hoa muon xoa khong ton tai!")
        return # Viet yeu cau nhap lai
    danhsachloaihanghoa.remove(xem_loaihanghoa())
