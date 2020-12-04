import sys
sys.stdin = open('가능한시험점수.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    # print(N)
    # print(scores)

    M = sum(scores)
    # 인덱스: 점수, value가 1이면 받을 수 있는 점수
    arr = [0] * (M + 1)

    arr[0] = 1
    for score in scores:
        for i in range(M, -1, -1):
            if arr[i] == 1:
                arr[i + score] = 1

    result = arr.count(1)
    print("#{} {}".format(tc, result))

