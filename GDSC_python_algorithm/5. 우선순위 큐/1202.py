import heapq
import sys

N, K = map(int,sys.stdin.readline().split())

jewels = []
bags = []
for _ in range(N):
    jewel= list(map(int,sys.stdin.readline().split()))
    heapq.heappush(jewels, jewel)

for _ in range(K):
    C = int(sys.stdin.readline())
    heapq.heappush(bags, C)


sum_price = 0



for _ in range(len(bags)):
    candidate = []
    bag = heapq.heappop(bags)
    for i in jewels:
        if bag >= i[0]:
            i[1] = -i[1]
            candidate.append(i)
    print(candidate)
        

    

print(sum_price)