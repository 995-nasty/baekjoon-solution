from decimal import Decimal

a,b,c,d = map(int, input().split())
x = ((a*c)%(2*b*d))

if x == 0:
    print(1)
else:
    print(0)