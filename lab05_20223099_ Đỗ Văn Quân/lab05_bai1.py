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

mean_all = np.mean(scores)
mean_students = np.mean(scores, axis=1)
mean_subjects = np.mean(scores, axis=0)
max_score = np.max(scores)
min_score = np.min(scores)
std_subjects = np.std(scores, axis=0)

best_student = np.argmax(mean_students)

print("Điểm trung bình toàn bộ:", mean_all)
print("Điểm trung bình từng sinh viên:", mean_students)
print("Điểm trung bình từng môn:", mean_subjects)
print("Điểm cao nhất:", max_score)
print("Điểm thấp nhất:", min_score)
print("Độ lệch chuẩn từng môn:", std_subjects)
print("Sinh viên có điểm TB cao nhất là vị trí:", best_student)