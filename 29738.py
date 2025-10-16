N = int(input())
for i in range(1,N+1):
    x = int(input())
    if x >4500:
        print("Case #%d: Round 1" %i)
    elif x > 1000:
        print("Case #%d: Round 2" %i)
    elif x > 25:
        print("Case #%d: Round 3" %i)
    else:
        print("Case #%d: World Finals" %i)