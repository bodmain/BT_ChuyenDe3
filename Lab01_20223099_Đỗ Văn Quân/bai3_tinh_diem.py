name = "Do Van Quan"
diem_qt = float(input("Nhap diem qt: "))
diem_thi = float(input("Nhap diem thi: "))
diem_tb = (0.4 * diem_qt)+ (0.6 * diem_thi)
print("Ho ten: ", name + "\nDiem trung binh: ", diem_tb)

if diem_tb >= 8.0:
    print("Xep loai: Gioi")
elif diem_tb >= 6.5:
    print("Xep loai: Kha")
elif diem_tb >= 5.0:
    print("Xep loai: Trung binh")
else:
    print("Xep loai: Chưa đạt")