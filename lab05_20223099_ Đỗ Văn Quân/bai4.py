import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

B = np.array([
    [4, 2],
    [1, 5]
])

print("A =")
print(A)
print("B =")
print(B)
print()

# 1. Tính A + B.
sum_AB = A + B
print("A + B =")
print(sum_AB)
print()

# 2. Tính A - B.
diff_AB = A - B
print("A - B =")
print(diff_AB)
print()

# 3. Tính tích ma trận A @ B.
product_AB = A @ B
print("A @ B =")
print(product_AB)
print()

# 4. Tính định thức của ma trận A.
det_A = np.linalg.det(A)
print("det(A) =", det_A)
print()

# 5. Tính ma trận nghịch đảo của A.
inv_A = np.linalg.inv(A)
print("A^-1 =")
print(inv_A)
print()

# 6. Giải hệ phương trình 2x + y = 5 và x + 3y = 7.
b = np.array([5, 7])
solution = np.linalg.solve(A, b)
print("Nghiệm hệ phương trình:", solution)
print()

# Kiểm tra nghiệm bằng cách thay vào hệ phương trình.
x, y = solution
lhs1 = 2*x + y
lhs2 = x + 3*y
print("Kiểm tra nghiệm:")
print("2x + y =", lhs1)
print("x + 3y =", lhs2)
print()

# Giải thích khi nào ma trận không khả nghịch:
print("Ma trận không khả nghịch khi định thức bằng 0.")
print("Trong trường hợp đó, hệ phương trình có thể vô số nghiệm hoặc không có nghiệm.")
