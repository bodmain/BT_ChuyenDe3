import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

idx = df.groupby("Lop")["DiemTB"].idxmax()
sv_max = df.loc[idx, ["HoTen", "Lop", "DiemTB"]]
print(sv_max)
