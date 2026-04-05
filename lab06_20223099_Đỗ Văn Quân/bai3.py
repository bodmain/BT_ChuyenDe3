import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")
print("5 dòng đầu:")
print(df.head())
print("\n5 dòng cuối:")
print(df.tail())
print("\nThông tin dữ liệu:")
print(df.info())
print("\nThống kê mô tả:")
print(df.describe())
print("\nKích thước dữ liệu:", df.shape)
print("Tên các cột:", df.columns.tolist())