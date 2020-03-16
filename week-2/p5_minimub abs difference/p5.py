import sys  
def find(A, B, C, p, q, r): 
    d=sys.maxsize 
    r1=0
    r2=0
    r3=0 
    i=0
    j=0
    k=0
    while(i < p and j < q and k < r): 
        mi=min(A[i], min(B[j], C[k])) 
        ma=max(A[i], max(B[j], C[k])); 
        if ma-mi<d: 
            r1=i 
            r2=j 
            r3=k 
            d=ma-mi; 
        if d==0: 
            break
        if A[i]==mi: 
            i = i+1
        elif B[j]==mi: 
            j = j+1
        else: 
            k = k+1
    print(max(A[r1],B[r2],C[r3])-min(A[r1],B[r2],C[r3]))
    print(A[r1], " ", B[r2], " ", C[r3]) 
while True:
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=list(map(int,input().split()))
    p=len(A) 
    q=len(B) 
    r=len(C) 
    find(A,B,C,p,q,r) 