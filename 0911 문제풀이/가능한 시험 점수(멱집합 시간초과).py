import sys
sys.stdin = open('가능한 시험 점수.txt')

def powerset(idx, sum):
    if idx >= N:
        case.add(sum)
        return
    powerset(idx + 1, sum + points[idx]) # 해당 인덱스 선택
    powerset(idx + 1, sum) # 해당 인덱스 미선택
    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 문제 개수
    points = list(map(int, input().split())) # 각 문제별 점수
    # print(N)
    # print(points)

    case = set()
    powerset(0, 0)
    result = len(case)

    print("#{} {}".format(tc, result))
