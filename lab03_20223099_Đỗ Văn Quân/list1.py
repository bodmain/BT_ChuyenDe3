# Danh sách sinh viên (mã SV, họ tên, điểm)
ds = [
    ("SV01", "Nguyen Van A", 8.5),
    ("SV02", "Tran Thi B", 7.0),
    ("SV03", "Le Van C", 9.2),
    ("SV04", "Pham Thi D", 6.5),
    ("SV05", "Hoang Van E", 5.0),
    ("SV06", "Nguyen Thi F", 8.0),
    ("SV07", "Do Van G", 4.5),
    ("SV08", "Le Thi H", 9.0)
]

# In danh sách
print("Danh sách sinh viên:")
for sv in ds:
    print(sv)

# SV điểm cao nhất
sv_max = max(ds, key=lambda x: x[2])
print("\nSinh viên điểm cao nhất:", sv_max)

# Điểm trung bình
dtb = sum(sv[2] for sv in ds) / len(ds)
print("Điểm trung bình:", dtb)

# SV >= 8
print("\nSinh viên >= 8:")
for sv in ds:
    if sv[2] >= 8:
        print(sv)