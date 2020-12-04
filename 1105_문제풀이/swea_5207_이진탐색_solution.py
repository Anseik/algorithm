import sys
sys.stdin = open('swea_5207_이진탐색_solution.txt')

# left, right : 시작 종료 인덱스
# target : 찾고자 하는 변수
# dir : 이전 단계에서 이동한 방향 (1: 왼쪽, 2: 오른쪽)
def binary_search(left, right, target, dir):
    global cnt
    if left > right:
        return
    mid = (left + right) // 2
    if A[mid] == target:
        # 도중에 리턴되지 않고 타켓을 찾았으면, 조건에 부합한다는 의미
        cnt += 1
        return
    elif A[mid] > target: # 왼쪽 검사
        if dir == 1:
            return
        return binary_search(left, mid - 1, target, 1)
    elif A[mid] < target: # 오른쪽 검사
        if dir == 2:
            return
        return binary_search(mid + 1, right, target, 2)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    # B에 속한 요소들이 A에 있는지 검사하면서 조건에 부합하는지 확인
    for target in B:
        if target in A: # i가 A에 포함된다면 조건에 부합하는지 검사
            # 이진 탐색 시작
            binary_search(0, N - 1, target, 0)

    print('#{} {}'.format(tc, cnt))