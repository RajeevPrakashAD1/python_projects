# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:24:29 2020

@author: acer
"""

n=int(input())
matrix=[]
for i in range (n):
    a=[]
    for k in range(n):
        a.append(int(input()))
    matrix.append(a)    
print(matrix)    