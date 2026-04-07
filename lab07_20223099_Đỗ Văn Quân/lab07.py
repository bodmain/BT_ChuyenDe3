import pandas as pd
import numpy as np

# Bài 1. Đọc dữ liệu và xem thông tin tổng quát
df = pd.read_csv("diem_sinhvien.csv")
print("Bài 1:")
print("5 dòng đầu:")
print(df.head())
print("\n5 dòng cuối:")
print(df.tail())
print("\nThông tin cấu trúc dữ liệu:")
print(df.info())
print("\nThống kê mô tả các cột số:")
print(df.describe())

# Bài 2. Tính điểm trung bình học phần
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
print("\nBài 2:")
print(df[["MaSV", "HoTen", "DiemTB"]].head())

# Bài 3. Xếp loại sinh viên theo điểm trung bình
def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)
print("\nBài 3:")
print(df[["HoTen", "DiemTB", "XepLoai"]].head())

# Bài 4. Thống kê mô tả điểm trung bình
print("\nBài 4:")
print("Trung bình:", df["DiemTB"].mean())
print("Lớn nhất:", df["DiemTB"].max())
print("Nhỏ nhất:", df["DiemTB"].min())
print("Độ lệch chuẩn:", df["DiemTB"].std())

# Bài 5. Thống kê tần suất dữ liệu
print("\nBài 5:")
print("Thống kê giới tính:")
print(df["GioiTinh"].value_counts())
print("\nThống kê lớp:")
print(df["Lop"].value_counts())
print("\nThống kê chuyên ngành:")
print(df["ChuyenNganh"].value_counts())
print("\nThống kê xếp loại:")
print(df["XepLoai"].value_counts())

# Bài 6. GroupBy theo lớp
tb_theo_lop = df.groupby("Lop")["DiemTB"].mean()
print("\nBài 6:")
print(tb_theo_lop)

# Bài 7. GroupBy theo giới tính
tb_theo_gt = df.groupby("GioiTinh")["DiemTB"].mean()
print("\nBài 7:")
print(tb_theo_gt)

# Bài 8. Tổng hợp nhiều chỉ tiêu bằng agg
tonghop = df.groupby("Lop")["DiemTB"].agg(["count", "mean", "max", "min"])
print("\nBài 8:")
print(tonghop)

# Bài 9. GroupBy nhiều điều kiện
baocao = df.groupby(["Lop", "GioiTinh"])["DiemTB"].agg(
    SoLuong="count",
    TrungBinh="mean",
    CaoNhat="max",
    ThapNhat="min"
)
print("\nBài 9:")
print(baocao)

# Bài 10. Pivot Table theo lớp và xếp loại
pivot1 = pd.pivot_table(
    df,
    index="Lop",
    columns="XepLoai",
    values="MaSV",
    aggfunc="count",
    fill_value=0
)
print("\nBài 10:")
print(pivot1)

# Bài 11. Crosstab theo lớp và giới tính
bang_cheo = pd.crosstab(df["Lop"], df["GioiTinh"])
print("\nBài 11:")
print(bang_cheo)

# Bài 12. Phân nhóm điểm học lực
bins = [0, 5, 7, 8.5, 10]
labels = ["<5", "5-6.9", "7-8.4", ">=8.5"]
df["NhomDiem"] = pd.cut(df["DiemTB"], bins=bins, labels=labels, right=False)
print("\nBài 12:")
print(pd.crosstab(df["Lop"], df["NhomDiem"]))

# Bài 13. Xếp hạng sinh viên trong từng lớp
df["XepHangTrongLop"] = df.groupby("Lop")["DiemTB"].rank(
    ascending=False,
    method="dense"
)
print("\nBài 13:")
print(
    df[["HoTen", "Lop", "DiemTB", "XepHangTrongLop"]]
    .sort_values(["Lop", "XepHangTrongLop"])
)

# Bài 14. Tìm sinh viên có điểm cao nhất của từng lớp
idx = df.groupby("Lop")["DiemTB"].idxmax()
sv_max = df.loc[idx, ["HoTen", "Lop", "DiemTB"]]
print("\nBài 14:")
print(sv_max)

# Bài 15. Phân tích tỷ lệ đỗ và trượt theo lớp
df["KetQua"] = np.where(df["DiemTB"] >= 4.0, "Do", "Truot")
so_luong = pd.crosstab(df["Lop"], df["KetQua"])
print("\nBài 15:")
print("Số lượng:")
print(so_luong)
ty_le = pd.crosstab(df["Lop"], df["KetQua"], normalize="index") * 100
print("\nTỷ lệ (%):")
print(ty_le.round(2))

# Bài 16. Báo cáo tổng hợp theo chuyên ngành
tong_hop_cn = df.groupby("ChuyenNganh").agg(
    SoSinhVien=("MaSV", "count"),
    DiemTrungBinh=("DiemTB", "mean")
)
tyle_ab = df[df["XepLoai"].isin(["A", "B"])].groupby("ChuyenNganh")["MaSV"].count()
tong_hop_cn["SoDatAB"] = tyle_ab
tong_hop_cn["SoDatAB"] = tong_hop_cn["SoDatAB"].fillna(0)
tong_hop_cn["TyLeDatAB"] = tong_hop_cn["SoDatAB"] / tong_hop_cn["SoSinhVien"] * 100
print("\nBài 16:")
print(tong_hop_cn.round(2))