import sys
import heapq


N = int(sys.stdin.readline())

cards = []

for _ in range(N):
    card = int(sys.stdin.readline())
    heapq.heappush(cards, card)

sum_card = 0

if N == 1:
    print(heapq.heappop(cards))
else:
    while cards:
        sum_card += heapq.heappop(cards)


print(sum_card)