# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:57:10 2024

@author: thuynhi_20033961
"""


a = float( input(" Nhập giá trị a: "))
b = float( input(" Nhập giá trị b: "))
c = float( input(" Nhập giá trị c: "))
if a + b>c and a+c>b and b+c>a:
    if a==b or b==c:
        print(" Đây là tam giác đều")
if a==b or b==c or a==c:
    print(" Đây là tam giác cân")
else:
        print("Đây là tam giác cân")
if( a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b):
        print("Đây là tam giác vuông.")
elif a**2> b**2 + c**2 or b**2 > a**2 + c**2 or c**2 == a**2 + b**2:
        print("Đây là tam giác tù" )
else: 
    print(" Đây là tam giác thường")
else:    
print("a,b,c không phải là cạnh của tam giác")    