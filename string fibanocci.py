# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:29:04 2020

@author: acer
"""

s1=input()
s2=input()
n=int(input())
sn=""
l=[]


    
for j in range(n):
    
    
    
    for i in range (len(s1)):
        if i==0 or i%2==0:
            if chr(ord(s1[i]))=='z':
                sn=sn+"a"
            else:
                sn=sn+chr(ord(s1[i])+1)
        else:
            if chr(ord(s2[i]))=='z':
                
                sn=sn+'a'
            else:
                sn=sn+chr(ord(s2[i])+1)
    
    l.append(sn) 
    print(l)
    s1=s2
    s2=sn
    sn=""
print(l[n-3])        
        