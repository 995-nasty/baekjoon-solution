N = int(input())
x = 0
for i in range(1,N+1):
    N = N-i
    if N <=0:
        N = N+i
        x = i
        break
if x %2 == 0:
    print("%d/%d" %(N,x+1-N))
else:
    print("%d/%d" %(x+1-N,N))

    