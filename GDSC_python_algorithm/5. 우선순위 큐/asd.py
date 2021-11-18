import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
heapq.heappush(heap, -71)
heapq.heappush(heap, -75)
print(heap)

sorted_heap = []

while heap:
  sorted_heap.append(heapq.heappop(heap))
print(sorted_heap)