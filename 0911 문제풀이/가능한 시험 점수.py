import sys
sys.stdin = open('가능한 시험 점수.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 문제 개수
    points = list(map(int, input().split())) # 각 문제별 점수

    # 0 ~ 최대점수까지 얻을 수 있는 점수를 체크하는 배열 생성
    arr = [0] * (sum(points) + 1)
    arr[0] = 1

    while points:
        c = points.pop(0)
        # 이미 만들어져 있는 점수 확인
        made = []
        for i in range(len(arr)):
            if arr[i] == 1:
                made.append(i)

        # 이미 만들어진 점수에 c를 더해 새로 만들 수 있는 점수 추가
        for m in made:
            arr[m + c] = 1

    result = arr.count(1)
    print("#{} {}".format(tc, result))
