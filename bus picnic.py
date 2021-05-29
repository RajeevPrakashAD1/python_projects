# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:13:46 2020

@author: acer
"""

ng= input()
ng=int(ng)
nsg=[int(x) for x in input().split()]


t=0      
for i in nsg:
    if 0<i<5:
        t=t+1
if t==len(nsg):
    
    
    
        
    count=0
    n1=nsg.count(1)
    n2=nsg.count(2)        
    n3=nsg.count(3) 
    n4=nsg.count(4)
    li=[n1,n2,n3,n4]

   
    
    count=count+n4
    s=n2%2    
    if s==0:
        
        count=count+(n2//2)
        
        
        nofdiff31= n3-n1
        if nofdiff31>0:
        
            count=count+n3
        if nofdiff31<0:
                
                count=count+n3
                rem1=n1-n3
                if rem1%4==0:
                
                    count=count+(rem1//4)
                else:
                    count=count+(rem1//4)+1
            
        if nofdiff31==0:
            count=count+n3
        
        
        
        
        
        
        
        
        
        
        
    if s==1:
        count=count+n2//2
        
    
         
          
          
          
        nofdiff31= n3-n1
        if nofdiff31>0:
            
            
        
            count=count+n3
            count=count+1
        if nofdiff31<0:
            
                
            count=count+n3
            count=count+1
            rem1=abs(nofdiff31)-2
            count=count+rem1-(rem1%4)
        if nofdiff31==0:
                
            count=count+n3
            
            count=count+1
            
    
    if ng>50 or ng<=0:
        print("invalid")
    else:
        print(count)
        
        
        