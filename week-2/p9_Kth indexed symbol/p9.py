def replace(n, k):
    if n == 1:
        return 0
    if k <= 2**(n-1)/2:
        return replace(n-1, k)
    else:
        return 1 - replace(n-1, k-2**(n-1)/2)
while True:
    n=int(input())
    k=int(input())
    print(replace(n,k))
