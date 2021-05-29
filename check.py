
n = int(input())

arr = list(map(int, input().rstrip().split()))




def insertionSort1(n, arr):
    l = []
    for i in range(n-1,0,-1 ):
        print(i)
        cont = True
        while arr[i] <arr[i-1] and cont:
            
            hold  = arr[i]
            arr[i] = arr[i-1]
            l.append(arr)
            print(l)
            arr[i-1] = hold
            print(arr)
            cont = False
    for k in l:
        print(*k,sep=" ")

    
         

print(insertionSort1(n,arr))

# print(p)
# for k in p:
#     print(*k,sep=" ")
