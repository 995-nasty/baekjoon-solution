import math as m

T = int(input())
for _ in range(T):
    X,Y,x,y,a,b = map(int, input().split())
    if X==x and Y==y:
        print(-1)
    k = (x-X)**2
    j = (y-Y)**2
    r =m.sqrt(k+j)
    R = a+b
    
    if r > R:
        print(2)
    elif r == R or :
        print(1)
    else:
        print(0)