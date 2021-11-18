import sys
import heapq


N = int(sys.stdin.readline())

cards = []

for _ in range(N):
    card = int(sys.stdin.readline())
    heapq.heappush(cards, card)

num = []

if N == 1:
    print(0)
else:
    while len(cards) > 1:
        sum_card = heapq.heappop(cards) + heapq.heappop(cards)
        num.append(sum_card)
        heapq.heappush(cards,sum_card)
    print(sum(num))

# N이 1이면 비교할 필요가 없는데 자꾸 한 묶음의 카드 수를 출력했음