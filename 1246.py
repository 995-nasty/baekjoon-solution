N, M = map(int, input().split())
x = []
for _ in range(M):
    x.append(int(input()))
    
x.sort()

mx = 0
a = 0
for i in range(M):
    if M-i-1 < N:
        if mx < x[i]*(M-i):
            mx = x[i]*(M-i)
            a = x[i]
    else:
        if mx < x[i]*N:
            mx = x[i]*N
            a = x[i]
print("%d %d" %(a,mx))
    