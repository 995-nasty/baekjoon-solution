N = int(input())
for j in range(N):
    x = list(input())
    for i in range(len(x)):
        if x[i] == "Z":
            x[i] = "A"
        else:
            x[i] = ord(x[i])+1
            x[i] = chr(x[i])
        
    print("String #%d" %(j+1))
    print("".join(x))

    if j !=N-1:
        print()
