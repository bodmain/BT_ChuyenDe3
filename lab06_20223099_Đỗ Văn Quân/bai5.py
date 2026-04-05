import pandas as pd

data = {
    "MaSV": ["SV01","SV02","SV03","SV04","SV05","SV06","SV07","SV08","SV09","SV10"],
    "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],
    "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],
    "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],
    "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9]
}

df = pd.DataFrame(data)
df["DiemTB"] = 0.3 * df["DiemCC"] + 0.7 * df["DiemCuoiKy"]

def nhom_hoc_tap(row):
    if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
        return "Tich cuc"
    elif row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
        return "Binh thuong"
    else:
        return "Can ho tro"

df["NhomHocTap"] = df.apply(nhom_hoc_tap, axis=1)
print(df)
print(df[(df["GioTuHoc"] > 2) & (df["SoBuoiNghi"] <= 2)])

# Nhận xét về xu hướng dữ liệu
print("\nNhận xét về xu hướng dữ liệu:")
print("1. Sinh viên có số giờ tự học cao (>3 giờ) thường có điểm chuyên cần và cuối kỳ cao.")
print("2. Số buổi nghỉ nhiều (>2 buổi) ảnh hưởng tiêu cực đến điểm số tổng thể.")
print("3. Nhóm 'Tích cực' có điểm trung bình cao nhất, cho thấy sự chăm chỉ dẫn đến kết quả tốt.")
print("4. Một số sinh viên cần hỗ trợ có điểm thấp do ít tự học và nghỉ nhiều.")
print("5. Sự kết hợp giữa giờ tự học và ít nghỉ học là yếu tố quan trọng cho thành công.")
print("6. Dữ liệu cho thấy mối tương quan tích cực giữa nỗ lực học tập và điểm số.")
print("7. Cần can thiệp sớm cho nhóm 'Cần hỗ trợ' để cải thiện kết quả học tập.")