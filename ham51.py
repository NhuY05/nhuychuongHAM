# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:36:17 2024

@author: Vivobook
Viết hàm kiểm tra giá trị nhập vào phải thuộc đoạn [-89, 90], nếu sai bắt
nhập lại.
"""

def ktgt():
    gtri = input("nhập giá trị: ")
    if gtri.replace(".","",1).replace("-", "",1).isdigit():
        gtri = float(gtri)
    if -86 <= gtri <= 90:
        return gtri
    print("k hợp lệ, nhập lại")
    return ktgt()
if __name__=="__main__":
    print(ktgt())