import sys
sys.stdin = open('피자굽기.txt')

T = int(input())
for tc in range(1, T+1):
    # 화덕의 크기 N, 피자 개수 M
    N, M = map(int, input().split())
    pizza = [0] + list(map(int, input().split())) # 1 ~ M번인덱스를 피자번호로 사용하기 위해 앞에 [0] 추가

    oven = [[i, pizza[i]] for i in range(1, N + 1)] # 피자 번호, 초기값(1 ~ N)
    remain = [[i, pizza[i]] for i in range(N + 1, M + 1)]
    # pos = N + 1 # 추가될 피자의 초기값 (N + 1) ~ M

    while len(oven) > 1:
        num, cheeze = oven.pop(0)
        cheeze = cheeze // 2
        if cheeze: # 치즈가 다 녹지 않았으면
            oven.append([num, cheeze])
        else:
            if remain:
                oven.append(remain.pop(0))

    print(oven[0][0])




