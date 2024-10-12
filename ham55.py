# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:13:49 2024

@author: Vivobook
"""

def cvhcn(dai,rong):
    return 2*(dai+rong)
def dthcn(dai,rong):
    return dai*rong
def vehcn(dai, rong):
    for _ in range(rong):
        print("*" * dai)
if __name__=="__main__":
    print(cvhcn(4, 3))
    print(dthcn(5, 6))
    print(vehcn(8,9))