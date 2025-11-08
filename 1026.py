N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort()
y.sort(reverse = True)

count = 0
for i in range(N):
    count += x[i]*y[i]
print(count)