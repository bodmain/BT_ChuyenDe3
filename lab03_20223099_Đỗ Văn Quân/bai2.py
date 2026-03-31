data = ["Python", "CSDL", "Python", "Java", "CSDL", "AI", "Python"]

# Loại trùng
unique = set(data)
print("Các môn học:", unique)

# Đếm số lần xuất hiện
count = {}
for mon in data:
    count[mon] = count.get(mon, 0) + 1

print("\nSố lần xuất hiện:", count)

# Môn nhiều nhất
max_mon = max(count, key=count.get)
print("Môn nhiều nhất:", max_mon)

# Sắp xếp giảm dần
sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
print("\nSắp xếp giảm dần:")
for mon, so_lan in sorted_count:
    print(mon, so_lan)