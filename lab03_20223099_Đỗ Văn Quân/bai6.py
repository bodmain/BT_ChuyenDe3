import csv

input_file = 'diemlop.csv'
error_file = 'loi.txt'

valid_rows = []
error_rows = []
line_num = 0

with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        line_num += 1
        masv = row.get('MaSV', '').strip()
        hoten = row.get('HoTen', '').strip()
        diem_raw = row.get('Diem', '').strip()

        try:
            diem = float(diem_raw)
        except ValueError:
            error_rows.append(f"Line {line_num+1}: {masv},{hoten},{diem_raw} - diem khong hop le (khong phai so)")
            continue

        if diem < 0 or diem > 10:
            error_rows.append(f"Line {line_num+1}: {masv},{hoten},{diem} - diem ngoai khoang 0-10")
            continue

        valid_rows.append((masv, hoten, diem))

# Tinh diem trung binh cua du lieu hop le
if valid_rows:
    avg = sum(d[2] for d in valid_rows) / len(valid_rows)
else:
    avg = 0.0

with open(error_file, 'w', encoding='utf-8') as f:
    for e in error_rows:
        f.write(e + '\n')

print(f'So dong hop le: {len(valid_rows)}')
print(f'So dong loi: {len(error_rows)}')
print(f'Diem TB hop le: {avg:.2f}')
