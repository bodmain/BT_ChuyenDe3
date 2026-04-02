import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 1. Tạo 100 bước ngẫu nhiên.
steps = np.random.choice([-1, 1], size=100)

# 2. Tính vị trí sau mỗi bước.
walk = np.cumsum(steps)

# 3. In 10 giá trị đầu tiên của dãy vị trí.
print("10 vị trí đầu tiên:", walk[:10])

# 4. Vẽ đồ thị random walk.
plt.figure()
plt.plot(walk, marker='o', markersize=4, linewidth=1)
plt.title("Random Walk 1 chiều")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Cho biết vị trí cuối cùng, vị trí lớn nhất và vị trí nhỏ nhất đạt được.
print("Vị trí cuối cùng:", walk[-1])
print("Vị trí lớn nhất:", np.max(walk))
print("Vị trí nhỏ nhất:", np.min(walk))

# Nâng cao: Mô phỏng 100 random walk, mỗi walk 100 bước.
steps_many = np.random.choice([-1, 1], size=(100, 100))
walks_many = np.cumsum(steps_many, axis=1)
final_positions = walks_many[:, -1]
print("Số walk kết thúc dương:", np.sum(final_positions > 0))

hit_10 = np.any(np.abs(walks_many) >= 10, axis=1)
print("Số walk chạm ngưỡng |10|:", np.sum(hit_10))
