import pandas as pd

data = {
    "MaSP": ["SP01","SP02","SP03","SP04","SP05","SP06"],
    "TenSP": ["Laptop","Chuot","Ban phim","USB","Loa","Webcam"],
    "TonDau": [5, 20, 15, 30, 10, 8],
    "NhapThem": [3, 10, 5, 20, 4, 2],
    "DaBan": [4, 18, 12, 35, 9, 3],
    "DonGia": [14500000,150000,300000,180000,750000,900000]
}

df = pd.DataFrame(data)
df["TonCuoi"] = df["TonDau"] + df["NhapThem"] - df["DaBan"]
df["GiaTriTonCuoi"] = df["TonCuoi"] * df["DonGia"]

print("Dữ liệu kho:")
print(df)

print("\nSản phẩm sắp hết hàng (TonCuoi <= 5):")
print(df[df["TonCuoi"] <= 5])

print("\nSản phẩm có giá trị tồn cuối lớn nhất:")
print(df.loc[df["GiaTriTonCuoi"].idxmax()])