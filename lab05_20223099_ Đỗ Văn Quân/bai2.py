import numpy as np

scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

print("Ma trận điểm:")
print(scores)
print()

# 1. Tính vector trung bình từng môn.
mean_col = np.mean(scores, axis=0)
print("Vector trung bình từng môn:", mean_col)

# 2. Tính vector độ lệch chuẩn từng môn.
std_col = np.std(scores, axis=0)
print("Vector độ lệch chuẩn từng môn:", std_col)

# 3. Chuẩn hóa toàn bộ ma trận bằng broadcasting (Z-score).
z_scores = (scores - mean_col) / std_col

# 4. In ma trận đã chuẩn hóa, làm tròn 2 chữ số thập phân.
print("Ma trận Z-score đã chuẩn hóa (làm tròn 2 chữ số):")
print(np.round(z_scores, 2))

# 5. Kiểm tra lại trung bình các cột sau chuẩn hóa có gần bằng 0 hay không.
print("TB các cột sau chuẩn hóa:", np.mean(z_scores, axis=0))

# Yêu cầu mở rộng: chuẩn hóa về khoảng [0, 1] theo từng môn.
min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)
scaled_01 = (scores - min_col) / (max_col - min_col)
print("\nMa trận chuẩn hóa về [0, 1] theo từng môn (làm tròn 2 chữ số):")
print(np.round(scaled_01, 2))
print("Giá trị min từng môn:", min_col)
print("Giá trị max từng môn:", max_col)
