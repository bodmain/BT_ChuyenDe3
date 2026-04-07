import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

df["KetQua"] = np.where(df["DiemTB"] >= 4.0, "Do", "Truot")
so_luong = pd.crosstab(df["Lop"], df["KetQua"])
print(so_luong)

ty_le = pd.crosstab(df["Lop"], df["KetQua"], normalize="index") * 100
print(ty_le.round(2))
