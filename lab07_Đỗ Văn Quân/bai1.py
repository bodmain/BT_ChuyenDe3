import pandas as pd
import numpy as np

# Đọc file CSV
df = pd.read_csv("diem_sinhvien.csv")

# Hiển thị 5 dòng đầu
print("===== 5 dòng đầu =====")
print(df.head())

# Hiển thị 5 dòng cuối
print("\n===== 5 dòng cuối =====")
print(df.tail())

# Xem thông tin cấu trúc dữ liệu
print("\n===== Thông tin DataFrame =====")
df.info()

# Xem thống kê mô tả các cột số
print("\n===== Thống kê mô tả =====")
print(df.describe())