import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [-i for i in works]
    heapq.heapify(works)
    while n > 0:
        heapq.heappush(works, heapq.heappop(works) + 1)
        n -= 1

    answer = 0
    for work in works:
        answer += (work ** 2)

    return answer


