import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

print("Trung bình:", df["DiemTB"].mean())
print("Lớn nhất:", df["DiemTB"].max())
print("Nhỏ nhất:", df["DiemTB"].min())
print("Độ lệch chuẩn:", df["DiemTB"].std())
