N = int(input())

count = 0
Ncount = 0
while True:
    if count == N:
        print(Ncount)
        break
    Ncount = str(Ncount+1)
    if Ncount.count("666") > 0:
        count +=1
    Ncount = int(Ncount)