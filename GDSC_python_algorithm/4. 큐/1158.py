import sys
from collections import deque

N = int(sys.stdin.readline())

card = list(range(1,N+1))
deq = deque(card)
discard = []

while len(deq) != 1:
    discard.append(str(deq.popleft()))
    deq.append(deq.popleft())

discard.append(str(deq.popleft()))

print(discard[-1])