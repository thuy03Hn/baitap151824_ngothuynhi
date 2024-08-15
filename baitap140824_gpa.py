# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:06:30 2024

@author: ngothuynhi_20033961
"""
gpa = float(input("Nhập điểm trung bình (GPA): "))
if gpa < 3.5: 
    print("Học lực Kém")
elif 3.5 <= gpa < 5.0:
    print("Học lực Yếu")
elif 5.0 <= gpa < 7.0:
    print("Học lực Trung bình")
elif 7.0 <= gpa < 8.0:
    print("Học lực Khá")
elif 8.0 <= gpa < 9.0:
    print("Học lực Giỏi")
elif 9.0 <= gpa <= 10.0:
    print("Học lực Xuất sắc")
else:
    print("GPA không hợp lệ, vui lòng nhập lại!")
