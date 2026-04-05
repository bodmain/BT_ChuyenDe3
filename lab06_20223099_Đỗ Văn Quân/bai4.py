import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.5:
        return "Trung binh"
    else:
        return "Yeu"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)
print(df[df["DiemTB"] >= 8])
df = df.rename(columns={"HoTen": "TenSinhVien"})
df = df.set_index("MaSV")
print(df)