import numpy as np

# Dữ liệu kho: tồn hiện tại, mức tồn tối thiểu, giá nhập dự kiến
current_stock = np.array([12, 5, 20, 3, 15, 8, 0, 18, 7, 10])
min_stock = np.array([10, 8, 15, 5, 12, 10, 5, 15, 10, 10])
unit_price = np.array([25.0, 10.0, 18.0, 30.0, 12.0, 22.0, 15.0, 8.0, 20.0, 11.0])
item_ids = np.arange(1, current_stock.size + 1)

if __name__ == '__main__':
    need_restock = current_stock < min_stock
    shortage_amount = np.maximum(min_stock - current_stock, 0)
    restock_cost = shortage_amount * unit_price

    print('1. Danh sách mặt hàng thiếu so với mức tối thiểu:')
    print('  ', item_ids[need_restock].tolist() if need_restock.any() else 'Không có')

    print('\n2. Số lượng cần nhập thêm từng mặt hàng:')
    for item, amount in zip(item_ids, shortage_amount):
        print(f'  Mặt hàng {item}: {amount}')

    print('\n3. Chi phí nhập thêm chỉ cho mặt hàng thiếu:')
    for item, need, cost in zip(item_ids, need_restock, restock_cost):
        if need:
            print(f'  Mặt hàng {item}: {cost:.0f}')

    total_cost = restock_cost.sum()
    print(f'\n4. Tổng chi phí nhập hàng: {total_cost:.0f}')

    status = np.where(need_restock, 'Thiếu hàng', 'Đủ hàng')
    print('\n5. Trạng thái mỗi mặt hàng:')
    for item, st in zip(item_ids, status):
        print(f'  Mặt hàng {item}: {st}')

    top3_shortage = np.argsort(shortage_amount)[::-1][:3]
    print('\n6. 3 mặt hàng thiếu nhiều nhất:')
    for rank, idx in enumerate(top3_shortage, start=1):
        print(f'  {rank}. Mặt hàng {item_ids[idx]}: thiếu {shortage_amount[idx]}')

    clipped_shortage = np.clip(shortage_amount, 0, 20)
    clipped_cost = clipped_shortage * unit_price
    print('\n7. Số lượng nhập sau giới hạn tối đa 20 đơn vị:')
    for item, amount in zip(item_ids, clipped_shortage):
        print(f'  Mặt hàng {item}: {amount}')

    clipped_total_cost = clipped_cost.sum()
    print(f'\n8. Tổng chi phí sau khi giới hạn: {clipped_total_cost:.0f}')

    print('\n9. Nhận xét:')
    if need_restock.sum() == 0:
        print('  Kho đang ổn định, không mặt hàng nào thiếu.')
    else:
        print(f'  Có {need_restock.sum()} mặt hàng thiếu. Nên ưu tiên nhập ngay các mặt hàng có thiếu lớn như', end=' ')
        print(', '.join(str(item_ids[idx]) for idx in top3_shortage if shortage_amount[idx] > 0) + '.')
        if (shortage_amount > 10).any():
            print('  Một số mặt hàng thiếu khá lớn, cần nhập bổ sung sớm.')
        else:
            print('  Thiếu ở mức vừa phải, có thể điều chỉnh đơn hàng theo kế hoạch.')
