def C(m,k):  
    f={}
    for i in m: 
        if (i in f): 
            f[i]+=1
        else: 
            f[i]=1
    for key, value in f.items(): 
        if(key==k):
            print(value) 
while True:
    m=list(map(int,input().split()))
    k=int(input())
    C(m,k)