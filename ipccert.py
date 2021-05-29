# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:22:50 2020

@author: acer
"""

N,M,K= [int(x) for x in input().split(" ")]
c=0
N=int(N)

M=int(M)
K=int(K)
for i in range (N):
    l=[int(x) for x in input().split(" ")]
    q=l[-1]
    summ=0
    for h in l[0:-1]:
        summ=summ+h
    if summ>M and q<10:
        c=c+1
print(c)