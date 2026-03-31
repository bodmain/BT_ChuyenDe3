# ================== BAI 1 ==================
print("\n===== BAI 1 =====")
ho_ten = "Do Van Quan"
ma_sv = "20223099"
lop = "CNTT15.01"
diem_cc = 8.5
diem_gk = 7.0

print("Ho ten:", ho_ten)
print("Ma sinh vien:", ma_sv)
print("Lop:", lop)
print("Diem chuyen can:", diem_cc)
print("Diem giua ky:", diem_gk)


# ================== BAI 2 ==================
print("\n===== BAI 2 =====")
diem_cc = 8.0
diem_gk = 7.5
diem_ck = 8.5

tong_ket = 0.1 * diem_cc + 0.3 * diem_gk + 0.6 * diem_ck
print("Diem tong ket:", round(tong_ket, 2))


# ================== BAI 3 ==================
print("\n===== BAI 3 =====")
tong_ket = 7.8

if tong_ket >= 8.5:
    xep_loai = "Gioi"
elif tong_ket >= 7.0:
    xep_loai = "Kha"
elif tong_ket >= 5.0:
    xep_loai = "Trung binh"
else:
    xep_loai = "Chua dat"

print("Xep loai:", xep_loai)


# ================== BAI 4 ==================
print("\n===== BAI 4 =====")
diem = [7.5, 8.0, 4.5, 6.0, 9.0, 5.5, 3.5]

tong = 0
dem_dat = 0

for x in diem:
    print(x)
    tong += x
    if x >= 5:
        dem_dat += 1

dtb = tong / len(diem)

print("Diem trung binh:", round(dtb, 2))
print("Diem lon nhat:", max(diem))
print("So diem dat:", dem_dat)


# ================== BAI 5 ==================
print("\n===== BAI 5 =====")
diem_input = float(input("Nhap diem tu 0 den 10: "))

while diem_input < 0 or diem_input > 10:
    print("Du lieu khong hop le, nhap lai!")
    diem_input = float(input("Nhap diem tu 0 den 10: "))

print("Diem hop le la:", diem_input)


# ================== BAI 6 ==================
print("\n===== BAI 6 =====")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "- so chan")
    else:
        print(i, "- so le")


# ================== BAI 7 ==================
print("\n===== BAI 7 =====")
ten = ["An", "Binh", "Chi", "Dung"]
diem = [7.5, 8.0, 6.5, 9.0]

tong = 0
dem_dat = 0

for i in range(len(ten)):
    print(ten[i], "-", diem[i])
    tong += diem[i]
    if diem[i] >= 5:
        dem_dat += 1

dtb = tong / len(diem)
max_diem = max(diem)
vi_tri = diem.index(max_diem)

print("Diem trung binh:", round(dtb, 2))
print("Sinh vien cao nhat:", ten[vi_tri])
print("So sinh vien dat:", dem_dat)

if dtb >= 8:
    print("Ket luan: Lop hoc tot")
elif dtb >= 6.5:
    print("Ket luan: Lop hoc kha")
else:
    print("Ket luan: Can cai thien")


# ================== BAI 8 ==================
print("\n===== BAI 8 =====")
ten = ["An", "Binh", "Chi", "Dung", "Ha"]
cc  = [8.0, 7.5, 9.0, 6.5, 8.5]
gk  = [7.0, 6.5, 8.5, 5.5, 7.5]
ck  = [8.5, 6.0, 9.0, 5.0, 8.0]

dem_kha_gioi = 0
tong_lop = 0

for i in range(len(ten)):
    tong_ket = 0.1 * cc[i] + 0.3 * gk[i] + 0.6 * ck[i]
    tong_lop += tong_ket

    if tong_ket >= 8.5:
        xep_loai = "Gioi"
    elif tong_ket >= 7.0:
        xep_loai = "Kha"
    elif tong_ket >= 5.0:
        xep_loai = "Trung binh"
    else:
        xep_loai = "Chua dat"

    if xep_loai == "Gioi" or xep_loai == "Kha":
        dem_kha_gioi += 1

    print(ten[i], "-", round(tong_ket, 2), "-", xep_loai)

print("Diem trung binh lop:", round(tong_lop / len(ten), 2))
print("So sinh vien Kha/Gioi:", dem_kha_gioi)


# ================== BAI 9 ==================
print("\n===== BAI 9 =====")
n = int(input("Nhap so luong sinh vien: "))

ten = []
diem = []

for i in range(n):
    ho_ten = input("Nhap ho ten sinh vien thu " + str(i + 1) + ": ")
    x = float(input("Nhap diem: "))

    while x < 0 or x > 10:
        print("Diem khong hop le. Nhap lai!")
        x = float(input("Nhap diem: "))

    ten.append(ho_ten)
    diem.append(x)

tong = 0
dem_dat = 0

for i in range(n):
    print(ten[i], "-", diem[i])
    tong += diem[i]
    if diem[i] >= 5:
        dem_dat += 1

dtb = tong / n
max_diem = max(diem)
min_diem = min(diem)

vi_tri_max = diem.index(max_diem)
vi_tri_min = diem.index(min_diem)

print("Sinh vien cao nhat:", ten[vi_tri_max], "-", max_diem)
print("Sinh vien thap nhat:", ten[vi_tri_min], "-", min_diem)
print("So sinh vien dat:", dem_dat)
print("Diem trung binh:", round(dtb, 2))

if dtb >= 8:
    print("Nhan xet: Lop hoc tot")
elif dtb >= 6.5:
    print("Nhan xet: Lop hoc kha")
else:
    print("Nhan xet: Can cai thien")