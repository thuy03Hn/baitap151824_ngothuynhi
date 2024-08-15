# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:16:55 2024

@author: DELL _ PC
"""

import math

a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))


delta = b**2 - 4*a*c


if a == 0:
    if b != 0:
        
        x = -c / b
        print(f"Nghiệm của phương trình là: x = {x}")
    else:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
else:
    if delta > 0:
        
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
       
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
      
        print("Phương trình vô nghiệm.")