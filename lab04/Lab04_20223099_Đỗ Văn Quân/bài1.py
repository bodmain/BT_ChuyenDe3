import numpy as np

# Dữ liệu mẫu: 10 sinh viên, cột điểm theo thứ tự [chuyên cần, giữa kỳ, thực hành, cuối kỳ]
score_matrix = np.array([
    [8.0, 7.5, 9.0, 8.5],
    [7.0, 6.0, 8.0, 7.2],
    [9.5, 8.0, 9.0, 9.0],
    [5.5, 5.0, 6.0, 5.8],
    [6.0, 4.5, 5.5, 6.0],
    [8.5, 9.0, 8.5, 8.8],
    [4.0, 6.0, 5.0, 4.8],
    [7.8, 7.2, 7.5, 7.0],
    [6.5, 7.0, 6.0, 6.8],
    [9.0, 8.5, 9.5, 9.2],
], dtype=float)

student_ids = np.arange(1, score_matrix.shape[0] + 1)

weights = np.array([0.1, 0.2, 0.3, 0.4])


def classify_score(total):
    if total >= 8.0:
        return "A"
    if total >= 6.5:
        return "B"
    if total >= 5.0:
        return "C"
    return "D"


def print_header(title):
    print("\n" + title)
    print("-" * len(title))


if __name__ == "__main__":
    print_header("1. Thông tin ma trận điểm")
    print("Ma trận điểm:\n", score_matrix)
    print("Shape:", score_matrix.shape)
    print("ndim:", score_matrix.ndim)
    print("dtype:", score_matrix.dtype)

    total_scores = score_matrix.dot(weights)
    print_header("2. Điểm tổng kết theo trọng số")
    for sid, total in zip(student_ids, total_scores):
        print(f"Sinh viên {sid}: {total:.2f}")

    categories = np.array([classify_score(total) for total in total_scores])
    print_header("3. Xếp loại sinh viên")
    for sid, total, cat in zip(student_ids, total_scores, categories):
        print(f"SV{sid}: {total:.2f} -> {cat}")

    max_index = np.argmax(total_scores)
    min_index = np.argmin(total_scores)
    print_header("4. SV có điểm cao nhất và thấp nhất")
    print(f"Cao nhất: SV{student_ids[max_index]} = {total_scores[max_index]:.2f}")
    print(f"Thấp nhất: SV{student_ids[min_index]} = {total_scores[min_index]:.2f}")

    filtered_above_7 = student_ids[total_scores >= 7.0]
    print_header("5. SV có điểm tổng kết >= 7.0")
    print("Danh sách SV:", filtered_above_7.tolist())

    has_below_5 = np.any(score_matrix < 5.0, axis=1)
    print_header("6. SV có ít nhất một điểm thành phần < 5.0")
    print("Danh sách SV:", student_ids[has_below_5].tolist())

    sort_desc = np.argsort(total_scores)[::-1]
    sorted_ids = student_ids[sort_desc]
    sorted_scores = total_scores[sort_desc]
    print_header("7. Sắp xếp điểm tổng kết giảm dần")
    for rank, (sid, score) in enumerate(zip(sorted_ids, sorted_scores), start=1):
        print(f"{rank}. SV{sid}: {score:.2f}")
    print("Top 3 SV:", sorted_ids[:3].tolist())

    final_scores = score_matrix[:, 3]
    mean_final = final_scores.mean()
    std_final = final_scores.std(ddof=0)
    z_scores = (final_scores - mean_final) / std_final
    print_header("8. Chuẩn hóa Z-score cho cột điểm cuối kỳ")
    for sid, raw, z in zip(student_ids, final_scores, z_scores):
        print(f"SV{sid}: điểm cuối kỳ = {raw:.2f}, Z-score = {z:.3f}")
    print(f"Mean = {mean_final:.3f}, Std = {std_final:.3f}")
    print("Nhận xét: ", end="")
    if std_final < 1.0:
        print("mức phân hóa thấp, điểm cuối kỳ khá tập trung quanh giá trị trung bình.")
    elif std_final < 1.5:
        print("mức phân hóa trung bình, có sự khác biệt vừa phải giữa các sinh viên.")
    else:
        print("mức phân hóa cao, có sự chênh lệch rõ rệt giữa các sinh viên.")
