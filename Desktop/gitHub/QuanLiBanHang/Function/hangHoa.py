import os

from Function.loaiHangHoa import xem_loaihanghoa, tao_loaihanghoa

danhsachhanghoa = []

def danhsach_hanghoa():
    files = os.listdir("QLBH/Data/HangHoa")
    if "hanghoa.csv" not in files:
        print("Danh sach hang hoa khong ton tai!")
        return

    with open('../LoaiHangHoa/hanghoa.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_read = line.split(',')
            if len(str_to_read) > 1:
                hanghoa = {}
                hanghoa["id"] = str_to_read[0]
                hanghoa["ten"] = str_to_read[1]
                hanghoa["idloaihanghoa"] = str_to_read[2]
                gia = str_to_read[3]
                if gia.endswith('\n'):
                    gia = gia[0:len(gia)-1]
                hanghoa["gia"] = gia
                danhsachhanghoa.append(gia)
            line = f.readline()

def xem_hanghoa(id=None):
    if id is None:
        id = input("Moi nhap ID hang hoa muon xem: ")
    for hanghoa in danhsachhanghoa:
        if id == hanghoa["id"]:
            return hanghoa

def tao_hanghoa():
    id = input("Nhap ID hang hoa muon tao: ")
    xet_id_daco = xem_hanghoa(id)
    if id is not None:
        print("ID hang hoa nay da co. Moi nhap lai!")
        ##Viet phan yeu cau nhap lai
        return
    hanghoa = {}
    hanghoa["id"] = id
    hanghoa["ten"] = input("Nhap ten hang hoa muon tao: ")
    idloaihanghoa = input("San pham nay thuoc loai hang hoa nao? ");
    xet_idloaihanghoa_daco = xem_loaihanghoa(idloaihanghoa)
    if xet_idloaihanghoa_daco is not None:
        hanghoa["idloaihanghoa"] = idloaihanghoa
    else:
        ask = input("Loai hang hoa nay khong ton tai. Ban co muon tao loai hang hoa moi khong? ")
        if ask == "y":
            tao_loaihanghoa()
            print("Da tao loai hang hoa moi.")
        else:
            break ## Hoac yeu cau nhap lai.
    str_to_save = hanghoa["id"]+','+hanghoa["ten"]+','+hanghoa["idloaihanghoa"]+','+hanghoa['gia']
    with open('../HangHoa/hanghoa.csv', 'a') as f:
        hanghoa = f.write(str_to_save)
    print("Da them thanh cong!!!")

def sua_hanghoa():
    id = input("Nhap ID hang hoa muon sua: ")
    xet_id_daco = xem_hanghoa(id)
    if id is None:
        print("Khong ton tai ID hang hoa nay!")
        return ## Hoac yeu cau nhap lai
    hanghoa = xem_hanghoa(id)
    hanghoa["id"] = id
    hanghoa["ten"] = input("Nhap ten hang hoa moi: ")
    idloaihanghoa = input("Hang hoa moi thuoc loai nao? ")
    xet_idloaihanghoa_daco = xem_loaihanghoa(idloaihanghoa)
    if xet_idloaihanghoa_daco is not None:
        hanghoa["idloaihanghoa"] = idloaihanghoa
    else:
        ask = input("Loai hang hoa nay khong ton tai. Ban co muon tao loai hang hoa moi khong? ")
        if ask == "y":
            tao_loaihanghoa()
            print("Da tao loai hang hoa moi.")
        else:
            break  ## Hoac yeu cau nhap lai.
    hanghoa["idloaihanghoa"] = idloaihanghoa
    hanghoa["gia"] = input("Moi nhap gia san pham moi: ")
    str_to_save = hanghoa["id"] + ',' + hanghoa["ten"] + ',' + hanghoa["idloaihanghoa"] + ',' + hanghoa['gia']
    with open('../HangHoa/hanghoa.csv', 'a') as f:
        hanghoa = f.write(str_to_save)
    print("Da sua thanh cong!!!")

def xoa_hanghoa():
    id = input("Nhap ID hang hoa muon sua: ")
    xet_id_daco = xem_hanghoa(id)
    if id is None:
        print("Khong ton tai ID hang hoa nay!")
        return  ## Hoac yeu cau nhap lai
    danhsachhanghoa.remove(xem_hanghoa(id))
    print("Da xoa thanh cong")