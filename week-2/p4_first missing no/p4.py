def getfirstmissing(a):
    if(a[1]-a[0]==1):
        return(getfirstmissing(a[1:]))
    else:
        return(a[0]+1)
arr=list(map(int,input().split()))
if(arr[0]!=1):
    print("1")
else:
    print(getfirstmissing(arr))