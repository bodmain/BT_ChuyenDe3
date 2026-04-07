import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

baocao = df.groupby(["Lop", "GioiTinh"])["DiemTB"].agg(
    SoLuong="count",
    TrungBinh="mean",
    CaoNhat="max",
    ThapNhat="min"
)
print(baocao)
