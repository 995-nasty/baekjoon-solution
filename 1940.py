"""이분탐색 사용"""

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
x = list(map(int, input().split()))
x.sort()

count = 0

for i in range(N):
    find = M - x[i]
    left = i+1
    right = N-1

    while left <= right:
        mid = (left + right)//2

        if x[mid] == find:
            count +=1
            break
        
        if find >= x[mid]:
            left = mid +1
        else:
            right = mid-1
        
print(count)        