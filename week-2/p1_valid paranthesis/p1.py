def paren(left,right,string):
    if(left == 0 and right == 0):
        print(string)
    if(left>right):
        return
    if (left > 0):
        paren(left-1,right,string+"(")
    if (right > 0):
        paren(left,right-1,string+")")
def par(n):
    paren(n/2,n/2,"")
while True:
    n=int(input())
    if(n%2!=0):
        print("invalid number")
    par(n)
    print("\n")