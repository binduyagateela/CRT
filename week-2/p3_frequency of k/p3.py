i=-1
def findleft(l,left,right,mid,key):
    global i
    mid=(left+right)//2
    if left>right:
        return
    if l[mid]==key:
        i=mid
    if l[mid]<key:
        findleft(l,mid+1,right,mid,key)
    else:
        findleft(l,left,mid-1,mid,key)
def findright(l,left,right,mid,key):
    global i
    mid=(left+right)//2
    if left>right:
        return
    if l[mid]==key:
        i=mid
    if l[mid]<=key:
        findright(l,mid+1,right,mid,key)
    else:
        findright(l,left,mid-1,mid,key)
while True:
    l=list(map(int,input().split()))
    n=len(l)
    l.sort()
    key=int(input())
    i=-1
    findleft(l,0,n-1,-1,key)
    a=i
    i=-1
    findright(l,0,n-1,-1,key)
    if a==i==-1:
        print(0)
    else:
        print(i-a+1)
