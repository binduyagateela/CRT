#a1 = [1, 12, 15, 26, 38]
#a2=[2, 13, 17, 30, 45]
while True:
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    a3=a1+a2
    a3.sort()
    l=len(a1)
    r=(a3[l-1]+a3[l])//2
    print(r)

