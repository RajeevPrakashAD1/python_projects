n = int(input())
l= []
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if i+j+k == n:
                
            
                    
                l.append((i,j,k))

nl=[]
passe = False
for kk in l:
    passe = False
    
    if kk[0] + kk[1] <kk[2] or kk[1] + kk[2] <kk[0] or kk[2] + kk[0] <kk[1]:
        passe = True
     
    
    if passe == True:
        nl.append((kk))
nnl = []        
for i in nl:
    
    p = {i[0],i[1],i[2]}
    nnl.append(p)
fl=[]
for ii in nnl:
    if ii not in fl:
        fl.append(ii)
        
print(nl)


print("______________________________________")
print(nnl)
print("___________________________________")
print(fl)
print(len(fl))        
    
print("___________________")
print(l)


