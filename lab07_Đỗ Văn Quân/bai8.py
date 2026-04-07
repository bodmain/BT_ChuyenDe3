import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

tonghop = df.groupby("Lop")["DiemTB"].agg(["count", "mean", "max", "min"])
print(tonghop)
