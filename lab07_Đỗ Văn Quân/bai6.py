import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

tb_theo_lop = df.groupby("Lop")["DiemTB"].mean()
print(tb_theo_lop)
