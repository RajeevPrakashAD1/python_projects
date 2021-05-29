# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:51:15 2020

@author: acer
"""

s=input(" ur str ")
for i in range (len(s)):
    p=s.count(s[i])
    
    for t in range (len(s)):
        
        if s[t]== s[i]:
            t=t+1
            
            if t <= 1 :
                
                print(s[i],'occurs: ',p)
        