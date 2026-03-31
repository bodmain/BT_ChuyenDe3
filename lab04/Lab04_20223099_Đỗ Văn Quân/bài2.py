import numpy as np

attendance = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
], dtype=int)

student_ids = np.arange(1, attendance.shape[0] + 1)

if __name__ == '__main__':
    # 1. Tổng số buổi đi học
    total_attended = attendance.sum(axis=1)
    print('1. Tổng buổi đi học mỗi sinh viên:')
    for sid, total in zip(student_ids, total_attended):
        print(f'  SV{sid}: {total}/8')

    # 2. Tỉ lệ chuyên cần
    attendance_rate = total_attended / attendance.shape[1] * 100
    print('\n2. Tỉ lệ chuyên cần (%):')
    for sid, rate in zip(student_ids, attendance_rate):
        print(f'  SV{sid}: {rate:.1f}%')

    # 3. Cảnh báo nếu < 75%
    warning_mask = attendance_rate < 75.0
    print('\n3. Sinh viên cảnh báo (chuyên cần < 75%):')
    print('  ', student_ids[warning_mask].tolist() if warning_mask.any() else 'Không có')

    # 4. Buổi học có nhiều vắng nhất
    absences_per_session = (attendance == 0).sum(axis=0)
    max_absences = absences_per_session.max()
    sessions_most_absent = np.where(absences_per_session == max_absences)[0] + 1
    print('\n4. Buổi có nhiều vắng nhất:')
    print(f'  Buổi: {sessions_most_absent.tolist()}, số vắng = {max_absences}')

    # 5. Sinh viên đi học đầy đủ cả 8 buổi
    perfect_attendance = student_ids[total_attended == 8]
    print('\n5. Sinh viên đi học đủ 8 buổi:')
    print('  ', perfect_attendance.tolist() if perfect_attendance.size else 'Không có')

    # 6. Sinh viên có ít nhất 2 buổi vắng liên tiếp
    consecutive_absences = []
    for sid, row in zip(student_ids, attendance):
        if '00' in ''.join(row.astype(str)):
            consecutive_absences.append(sid)
    print('\n6. Sinh viên có >= 2 buổi vắng liên tiếp:')
    print('  ', consecutive_absences if consecutive_absences else 'Không có')

    # 7. Nhận xét ngắn về ý thức học tập
    absent_counts = (attendance == 0).sum(axis=1)
    active_students = (attendance_rate >= 75.0).sum()
    perfect_count = perfect_attendance.size
    if absent_counts.mean() <= 1:
        comment = 'Lớp có ý thức học tập tốt, hầu hết sinh viên đi học đều đặn.'
    elif absent_counts.mean() <= 2:
        comment = 'Ý thức tương đối tốt nhưng cần duy trì đều đặn hơn đối với một số sinh viên.'
    else:
        comment = 'Cần nhắc nhở thêm vì vẫn còn nhiều sinh viên vắng học.'
    print('\n7. Nhận xét:')
    print('  ', comment)
    print(f'  Số SV trên 75% chuyên cần: {active_students}/12, số SV đi học đủ 8 buổi: {perfect_count}')
