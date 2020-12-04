import sys
sys.stdin = open('가능한 시험 점수.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    points = list(map(int, input().split()))
    l = sum(points) + 1
    arr = [0] * l
    arr[0] = 1

    for i in points:
        # 뒤에서 부터 순회하면 i를 중복해서 더하는 것을 피할 수 있다.
        for j in range(l - 1, -1, -1):
            if arr[j]:
                arr[j + i] = 1
    print("#{} {}".format(tc, arr.count(1)))