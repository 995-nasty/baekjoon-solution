from queue import Queue

que = Queue()

N = int(input())
for i in range(1,N+1):
    que.put(i)

while que.qsize() > 1:
    print(que.get(), end=" ")
    que.put(que.get())
print(que.get())