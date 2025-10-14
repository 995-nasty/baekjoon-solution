N,M = map(int, input().split())
gong = [x for x in range(1,N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    T = gong[a-1]
    gong[a-1] = gong[b-1]
    gong[b-1] = T

print(*gong)