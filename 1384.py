group = 1

while True:
    N = int(input())
    if N == 0:
        break
    x = []
    y = []
    for _ in range(N):
        a = list(map(str, input().split()))
        x.append(a[0])
        y.append(a[1:])
    count = 0
    print("Group %d" %(group))
    for i in range(N):
        for j in range(N-1):
            if y[i][j] == "N":
                count +=1
                if i > j:
                    print("%s was nasty about %s" %(x[i-j-1],x[i]))
                else:
                    print("%s was nasty about %s" %(x[i+N-j-1],x[i]))
    if count == 0:
        print("Nobody was nasty")
    group +=1
            
        
        
        
        
        
        