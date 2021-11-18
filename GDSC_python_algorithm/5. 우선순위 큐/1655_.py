import sys
import heapq

N = int(sys.stdin.readline())


max_heap = [] # 왼쪽
min_heap = [] # 오른쪽

for _ in range(N):
    num = int(sys.stdin.readline())
    
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num,num))
    else:
        heapq.heappush(min_heap, (num,num))

    if len(min_heap) == 0:
        pass

    elif max_heap[0][1] > min_heap[0][1] :
        min = heapq.heappop(min_heap)[1]
        max = heapq.heappop(max_heap)[1]

        heapq.heappush(min_heap,(max, max))
        heapq.heappush(max_heap,(-min, min))

    print(max_heap[0][1])

# 힙 정렬을 통한 방법은 성공하지 못함 ㅠ