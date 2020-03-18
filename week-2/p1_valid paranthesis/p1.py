c=0
def solution(left,right,string):
    global c
    if(left == 0 and right == 0):
        print(string)
        c+=1
    if(left>right):
        return
    if (left > 0):
        solution(left-1,right,string+"(")
    if (right > 0):
        solution(left,right-1,string+")")
def paranthesis(n):
    solution(n/2,n/2,"")
while True:
    n=int(input())
    if(n%2!=0):
        print("invalid number")
    paranthesis(n)
    print(c)
    print("\n")