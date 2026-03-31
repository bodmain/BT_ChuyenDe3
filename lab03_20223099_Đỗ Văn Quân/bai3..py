diem = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 8.5, 3.0]

# Điểm đạt
dat = [d for d in diem if d >= 5]
print("Điểm đạt:", dat)

# Bình phương
binh_phuong = [d**2 for d in dat]
print("Bình phương:", binh_phuong)

# Xếp loại
xep_loai = {
    i+1: ("A" if d >= 8 else "B" if d >= 6.5 else "C" if d >= 5 else "F")
    for i, d in enumerate(diem)
}

print("Xếp loại:")
for k, v in xep_loai.items():
    print(f"SV{k}: {v}")