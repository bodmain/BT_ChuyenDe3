def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số SV: "))
    for i in range(n):
        ma = input("Mã: ")
        ten = input("Tên: ")
        diem = float(input("Điểm: "))
        ds.append((ma, ten, diem))
    return ds

def tinh_diem_trung_binh(ds):
    return sum(sv[2] for sv in ds) / len(ds)

def tim_sv_max(ds):
    return max(ds, key=lambda x: x[2])

def xep_loai(diem):
    if diem >= 8:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5:
        return "C"
    else:
        return "F"

def in_bao_cao(ds):
    print("\n--- BÁO CÁO ---")
    for sv in ds:
        print(sv, "- Xếp loại:", xep_loai(sv[2]))
    print("Điểm TB:", tinh_diem_trung_binh(ds))
    print("SV cao nhất:", tim_sv_max(ds))


# MAIN
ds = nhap_danh_sach()
in_bao_cao(ds)