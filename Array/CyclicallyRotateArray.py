def rotatearr(a):
    a[:]=a[len(a)-1:]+a[:len(a)-1]
    return a
a=list(map(int,input().split(" ")))
print(rotatearr(a))
    
