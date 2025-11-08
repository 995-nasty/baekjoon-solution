N, M = map(int, input().split())
try:
    x = list(map(int, input().split()))
    count = 0
    box = 0
    for i in range(N):
        count +=x[i]
        if count > M:
            box +=1
            count = x[i]
    if count > 0:
        box +=1    
    print(box)
except:
    print(0)