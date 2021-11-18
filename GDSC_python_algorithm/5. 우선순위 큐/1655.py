import sys
import heapq

N = int(sys.stdin.readline())

heap_num = []
heap_sorted = []
heap_new = []

for _ in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(heap_num, x)
    heap_new = heap_num
    heap_sorted = []

    while heap_new:
        heap_sorted.append(heapq.heappop(heap_new))
    
    print(heap_sorted)
    if len(heap_sorted)%2 == 1:
        print(heap_sorted[(len(heap_sorted)//2)])    
    else:
        print(heap_sorted[int((len(heap_sorted)/2))-1])