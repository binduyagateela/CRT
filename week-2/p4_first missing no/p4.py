def f(a,l): 
    for i in range(l): 
        if ((a[i])- 1<l and a[(a[i])-1]>0): 
            a[(a[i])-1]=-a[(a[i])-1] 
    for i in range(l): 
        if (a[i]>0): 
            return i+1
    return l+1    
arr=list(map(int,input().split()))
l= len(arr)  
m=f(arr,l)  
print(m)