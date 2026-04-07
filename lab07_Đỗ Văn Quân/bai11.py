import pandas as pd
import numpy as np

df = pd.read_csv("diem_sinhvien.csv")

bang_cheo = pd.crosstab(df["Lop"], df["GioiTinh"])
print(bang_cheo)
