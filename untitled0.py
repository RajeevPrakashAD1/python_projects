# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:49:40 2020

@author: acer
"""

t=int(input("test cases"))
sm=[]
if 1<=t<=1000:
    
    for i in range (t):
        n=input(" no of dish")
        
        cl=[int(x) for x in input().split()]
        cl.sort(key =int)
        
        if n==1:
            print(cl[0])
            break
        if n==2:
            print(max(cl))
            break
        
        if n==3:
            if max(cl)>=sum(cl):
                print(max(c1))
                break        
            else:
            
            
                for k in range (len(cl)):
                    for j in range(len(cl)):
                        if cl[k]+cl[j]>=sum(cl)-cl[k]-cl[j] :
                            
                            
                            print(cl[k]+cl[j])
                            break
                        break
        
         elif n>3:
              for k in range (len(cl)):
                    for j in range(len(cl)):
                        if cl[k]+cl[j]>=sum(cl)-cl[k]-cl[j] :
                            
                        
                        print(cl[k]+cl[j])
                        break
         
        



