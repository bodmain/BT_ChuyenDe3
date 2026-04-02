import pandas as pd
import numpy as np

# Phần 1: Mô phỏng quy trình thu thập và chuẩn hóa dữ liệu
print("--- Phần 1: Mô tả quy trình thu thập dữ liệu ---")
print("1. Mục tiêu: phân tích ảnh hưởng của thời gian tự học và thời gian dùng mạng xã hội đến điểm trung bình.")
print("2. Đối tượng: sinh viên năm 2 và năm 3 của một ngành học cụ thể.")
print("3. Phiếu khảo sát: MaSV, Tuoi, GioiTinh, GioTuHoc, GioMangXaHoi, DiemTB.")
print("4. Thu thập dữ liệu thô từ Google Form / Excel / CSV.")
print("5. Kiểm tra chất lượng: thiếu, trùng, định dạng không đồng bộ, ngoại lệ.")
print("6. Chuẩn hóa dữ liệu và lưu dữ liệu sạch.")
print()

# Phần 2: Dữ liệu thô ban đầu
print("--- Phần 2: Dữ liệu thô ban đầu ---")
data = {
    "MaSV": ["SV01", "SV02", "SV03", "SV03", "SV05", "SV06", "SV07", "SV08"],
    "Tuoi": [20, 21, 19, 19, None, 22, 35, 20],
    "GioiTinh": ["Nam", "Nữ", "nu", "nu", "Nam", "Nữ", "Nam", None],
    "GioTuHoc": [2.5, 3, None, 4, 2, 10, -1, 3.5],
    "GioMangXaHoi": [4, 5, 3.5, 3.5, 20, 2, 5, None],
    "DiemTB": [3.1, 2.8, 3.5, 3.5, 2.0, 3.8, 4.5, None]
}

df = pd.DataFrame(data)
print(df)
print()

# Phần 3: Xử lý dữ liệu
print("--- Phần 3: Xử lý dữ liệu ---")
print("Kích thước dữ liệu:", df.shape)
print("Dữ liệu thiếu theo cột:\n", df.isnull().sum())
print()

# 3. Xóa bản ghi trùng lặp theo MaSV
print("Xóa bản ghi trùng theo MaSV...")
df = df.drop_duplicates(subset="MaSV")
print("Kích thước sau khi xóa trùng:", df.shape)
print()

# 5. Chuẩn hóa cột GioiTinh
print("Chuẩn hóa GioiTinh...")
df["GioiTinh"] = df["GioiTinh"].replace({
    "nu": "Nữ",
    "Nữ": "Nữ",
    "Nam": "Nam"
})
df["GioiTinh"] = df["GioiTinh"].fillna("Không rõ")

# 4. Điền dữ liệu thiếu bằng giá trị trung bình cho các biến số số
for col in ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]:
    mean_value = df[col].mean()
    df[col] = df[col].fillna(mean_value)

print("Dữ liệu sau điền giá trị thiếu:")
print(df)
print()

# 6. Phát hiện dữ liệu bất thường
print("Phát hiện dữ liệu bất thường:")
abnormal_conditions = {
    "Tuoi": df["Tuoi"] > 30,
    "GioTuHoc": df["GioTuHoc"] < 0,
    "GioMangXaHoi": df["GioMangXaHoi"] > 12,
    "DiemTB": df["DiemTB"] > 4.0
}
for col, cond in abnormal_conditions.items():
    if cond.any():
        print(f"- {col}:", df.loc[cond, ["MaSV", col]].to_dict(orient="records"))
    else:
        print(f"- {col}: không có giá trị bất thường")
print()

# 7. Thay giá trị bất thường bằng giá trị trung bình hợp lý
print("Thay giá trị bất thường bằng giá trị trung bình hợp lý của cột tương ứng...")
for col, cond in abnormal_conditions.items():
    mean_value = df.loc[~cond, col].mean()
    df.loc[cond, col] = mean_value

print("Dữ liệu sau thay giá trị bất thường:")
print(df)
print()

# 8. Tạo bộ dữ liệu sạch và in kết quả sau xử lý
clean_df = df.copy()
print("--- Dữ liệu sạch ---")
print(clean_df)
print()

# 9. Chuẩn hóa các biến số theo Min-Max
cols = ["Tuoi", "GioTuHoc", "GioMangXaHoi", "DiemTB"]
minmax_df = clean_df.copy()
for col in cols:
    minmax_df[col] = (minmax_df[col] - minmax_df[col].min()) / (minmax_df[col].max() - minmax_df[col].min())
print("Dữ liệu Min-Max:")
print(minmax_df)
print()

# 10. Chuẩn hóa các biến số theo Z-score
zscore_df = clean_df.copy()
for col in cols:
    zscore_df[col] = (zscore_df[col] - zscore_df[col].mean()) / zscore_df[col].std()
print("Dữ liệu Z-score:")
print(zscore_df)
print()

# 11. So sánh dữ liệu trước và sau chuẩn hóa, nêu nhận xét ngắn
print("--- Nhận xét ---")
print("- Dữ liệu thô chứa bản ghi trùng, thiếu và giá trị bất thường, nên cần làm sạch trước khi phân tích.")
print("- Sau khi làm sạch, các biến số số đã được điền thiếu và xử lý ngoại lệ.")
print("- Min-Max chuẩn hóa các cột vào khoảng [0, 1], phù hợp cho mô hình cần giới hạn thang đo.")
print("- Z-score chuẩn hóa các cột để trung bình bằng 0 và độ lệch chuẩn bằng 1, phù hợp cho phân tích sử dụng khoảng cách.")
print("- Chuẩn hóa giúp so sánh hợp lý giữa các biến số có đơn vị và thang đo khác nhau.")
