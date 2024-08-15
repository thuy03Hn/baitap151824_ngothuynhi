# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:08:11 2024

@author: thuynhi_20033961
"""
a = float(input(" Nhập giá trị a: "))
b = float(input(" Nhập giá trị b: "))
if a !=0:
    x = -b/a
    print(f"Nghiệm của phương trình là: x={x}")
if b == 0:
    print("Phương trình vô số nghiệm")
else:
    print(" Phương trình vô nghiệm")
