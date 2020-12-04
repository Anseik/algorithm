# 최소힙만 지원(heapq)
import heapq
heap = [7, 2, 5, 3, 4, 6]
print(heap)
heapq.heapify(heap) # 힙으로 만든다.
print(heap)
heapq.heappush(heap, 1) # 요소를 추가한다.
print(heap)
while heap:
    print(heapq.heappop(heap), end = " ") # 요소를 뺀다.
print()
####################################################
# 그럼 최대힙은 어떻게 하는가? -(마이너스)붙여서 힙으로 만들고 pop할때 -를 곱해서 원상복구 한다.
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i]))
print(heap2)
heapq.heappush(heap2, (-1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2) * -1, end = " ")