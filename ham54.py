# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:11:42 2024

@author: Vivobook
"""

def fib(n):
    a,b = 0,1
    while a<n:
        print(a, end="\t")
        a,b = b, a+b
if __name__=="__main__":
    print(fib(1000))