import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

bins = [0, 5, 7, 8.5, 10]
labels = ["<5", "5-6.9", "7-8.4", ">=8.5"]
df["NhomDiem"] = pd.cut(df["DiemTB"], bins=bins, labels=labels, right=False)
print(pd.crosstab(df["Lop"], df["NhomDiem"]))
