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
ket_qua = df[df["XepLoai"].isin(["Gioi", "Kha"])]
ket_qua = ket_qua.sort_values(by="DiemTB", ascending=False)
ket_qua.to_csv("ketqua_xuly.csv", index=False, encoding="utf-8-sig")
print(ket_qua)
print("Da luu file ketqua_xuly.csv")