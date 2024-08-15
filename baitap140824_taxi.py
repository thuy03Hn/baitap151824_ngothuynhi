# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:31:05 2024

@author: DELL _ PC
"""

# Tính tiền taxi theo số km quãng đường đi được. Cho biết:
#• 1 km đầu tiên: 20k
#• 3 km đầu tiên: 13k/km
#• Từ km thứ 4 đến km thứ 8: 12k/km
#• Còn lại giá 10k/km
#• Nếu đi hơn 100k thì giảm thêm 8% cho tổng tiền.
km = float(input("Nhập số km quãng đường đi được: "))

total_cost = 0

if km <= 1:
    total_cost = 20 * km
elif km <= 4:
    total_cost = 20 + (km - 1) * 13
elif km <= 8:
    total_cost = 20 + 3 * 13 + (km - 4) * 12
else:
    total_cost = 20 + 3 * 13 + 4 * 12 + (km - 8) * 10


if total_cost > 100:
    total_cost *= 0.92


print(f"Tổng tiền taxi: {total_cost:.2f}k VND")