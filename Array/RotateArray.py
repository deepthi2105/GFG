def rotatearr(a,k):
    a[:]=a[k:]+a[:k]
    return a
t=int(input())
for i in range(t):
    li=list(map(int,input().split(" ")))
    n=li[0]
    k=li[1]
    a=list(map(int,input().split(" ")))
    print(rotatearr(a,k))
