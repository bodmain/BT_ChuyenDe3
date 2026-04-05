import pandas as pd

data = {
    "MaKH": ["KH01","KH02","KH03","KH04","KH05","KH06","KH07","KH08"],
    "TenKH": ["Lan","Minh","Hung","Ha","Phuong","Toan","Ngoc","Tuan"],
    "SoDonHang": [12, 5, 8, 15, 4, 10, 6, 3],
    "TongChiTieu": [25000000, 7200000, 12500000, 31000000, 4300000, 9800000, 15000000, 2800000]
}

df = pd.DataFrame(data)

def xep_loai(tien):
    if tien >= 20000000:
        return "VIP"
    elif tien >= 10000000:
        return "Than thiet"
    elif tien >= 5000000:
        return "Tiem nang"
    else:
        return "Thuong"

df["XepLoaiKH"] = df["TongChiTieu"].apply(xep_loai)

print("Khách hàng VIP và Than thiet:")
print(df[df["XepLoaiKH"].isin(["VIP", "Than thiet"])])

print("\nDanh sách sắp xếp theo TongChiTieu giảm dần:")
print(df.sort_values(by="TongChiTieu", ascending=False))

print("\nChi tiêu trung bình:", df["TongChiTieu"].mean())