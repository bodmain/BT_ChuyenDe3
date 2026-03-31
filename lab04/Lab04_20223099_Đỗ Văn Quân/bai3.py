import numpy as np

# Doanh thu của 5 sản phẩm trong 7 ngày
# Mỗi hàng là sản phẩm, mỗi cột là ngày
revenue = np.array([
    [1200, 1300, 1250, 1400, 1350, 1500, 1450],
    [900, 950, 980, 1020, 1000, 1050, 1100],
    [1500, 1400, 1450, 1480, 1520, 1550, 1600],
    [700,  680,  720,  750,  730,  760,  780],
    [1100, 1150, 1120, 1180, 1200, 1220, 1250],
], dtype=float)

product_ids = np.arange(1, revenue.shape[0] + 1)

def print_header(title):
    print("\n" + title)
    print("-" * len(title))


if __name__ == '__main__':
    # 1. Tổng doanh thu theo từng ngày
    daily_revenue = revenue.sum(axis=0)
    print_header('1. Tổng doanh thu theo từng ngày')
    for day, total in enumerate(daily_revenue, start=1):
        print(f'  Ngày {day}: {total:.0f}')

    # 2. Tổng doanh thu và trung bình theo sản phẩm
    product_total = revenue.sum(axis=1)
    product_mean = revenue.mean(axis=1)
    print_header('2. Tổng và doanh thu trung bình của từng sản phẩm')
    for pid, tot, avg in zip(product_ids, product_total, product_mean):
        print(f'  SP{pid}: tổng = {tot:.0f}, trung bình = {avg:.1f}')

    # 3. Ngày và sản phẩm tốt nhất
    best_day = np.argmax(daily_revenue) + 1
    best_product = np.argmax(product_total) + 1
    print_header('3. Ngày doanh thu cao nhất và sản phẩm bán tốt nhất')
    print(f'  Ngày cao nhất: Ngày {best_day} với {daily_revenue[best_day-1]:.0f}')
    print(f'  Sản phẩm tốt nhất: SP{best_product} với tổng {product_total[best_product-1]:.0f}')

    # 4. Điều chỉnh tăng 8% cho sản phẩm 2 và 5
    adjusted_revenue = revenue.copy()
    adjusted_revenue[[1, 4], :] *= 1.08
    print_header('4. Doanh thu sau điều chỉnh tăng 8% cho SP2 và SP5')
    print(adjusted_revenue)

    # 5. So sánh tổng doanh thu tuần trước và sau điều chỉnh
    weekly_total_before = revenue.sum()
    weekly_total_after = adjusted_revenue.sum()
    print_header('5. So sánh tổng doanh thu toàn tuần')
    print(f'  Trước điều chỉnh: {weekly_total_before:.0f}')
    print(f'  Sau điều chỉnh:  {weekly_total_after:.0f}')
    print(f'  Tăng thêm:       {weekly_total_after - weekly_total_before:.0f}')

    # 6. Ngày có tổng doanh thu lớn hơn mức trung bình toàn tuần
    weekly_average = daily_revenue.mean()
    above_avg_days = np.where(daily_revenue > weekly_average)[0] + 1
    print_header('6. Ngày có tổng doanh thu > trung bình toàn tuần')
    print(f'  Ngày: {above_avg_days.tolist()}, trung bình toàn tuần = {weekly_average:.1f}')

    # 7. Sản phẩm ổn định nhất theo độ lệch chuẩn
    product_std = revenue.std(axis=1, ddof=0)
    most_stable_product = np.argmin(product_std) + 1
    print_header('7. Sản phẩm có độ ổn định cao nhất')
    for pid, std in zip(product_ids, product_std):
        print(f'  SP{pid}: độ lệch chuẩn = {std:.1f}')
    print(f'  SP{most_stable_product} là ổn định nhất')

    # 8. Nhận xét sản phẩm ưu tiên bán
    prioritized = np.argmax(product_total) + 1
    print_header('8. Nhận xét sản phẩm nên ưu tiên bán')
    print(f'  Nên ưu tiên SP{prioritized} vì có tổng doanh thu toàn tuần cao nhất và tăng trưởng ổn định.')
