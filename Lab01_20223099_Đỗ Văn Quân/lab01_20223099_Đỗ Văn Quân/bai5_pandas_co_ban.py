import pandas as pd

data = {
    "MaSV": ["SV001", "SV002", "SV003"],
    "HoTen": ["Nguyen Van An", "Tran Thi Bắc", "Le Van Nam"],
    "Lop": ["KTPM1", "KTPM2", "KTPM1"],
    "Diem": [8.5, 7.0, 9.0]
}
df = pd.DataFrame(data)
print("Toàn bộ bảng dữ liệu:")
print(df)

print("\nHai dòng đầu tiên:")
print(df.head(2))

print("\nTên các cột:")
print(df.columns)

print("\nĐiểm trung bình:")
print(df["Diem"].mean())