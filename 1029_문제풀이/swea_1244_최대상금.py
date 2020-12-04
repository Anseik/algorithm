import sys
sys.stdin = open('swea_1244_최대상금.txt')


def change():
    global cnt
    for i in range(N - 1):
        idx = i # 교환할 인덱스 i이면 교환 안 한다.
        for j in range(i, N):
            if numbers[idx] < numbers[j]: # 뒤에 큰것이 있으면
                idx = j
            # 현재 교환할 대상이 자기자신이 아니고 중복되는 값이 있는경우 더 뒤에 있는 것과 교환
            elif numbers[idx] == numbers[j] and idx != i:
                idx = j
        if idx != i:
            numbers[i], numbers[idx] = numbers[idx], numbers[i]
            cnt += 1
            if cnt == switch:
                return


T = int(input())
for tc in range(1, T + 1):
    numbers, switch = input().split()
    numbers = list(map(str, numbers))
    switch = int(switch)
    # print(numbers, switch)
    N = len(numbers)

    cnt = 0

    change()
    rest = switch - cnt
    if rest % 2 == 0: # 남은 교환횟수가 짝수일때
        print('#{} {}'.format(tc, ''.join(numbers)))
    else: # 남은 교환횟수가 홀수일때
        for k in range(N):
            pass
        print('#{} {}'.format(tc, '교환을 더하세요'))


    # 선택정렬 알고리즘
    # 주어진 switch 횟수만큼 반복한다.
    # 앞에서부터 뒤에 자신보다 큰 수가 있으면 교환한다.
    # 교환할 수 있는 숫자가 여러개면 가장 큰수와 교환한다.
    # 중복되는 숫자가 있을 경우 더 뒤에 있는 숫자와 교환한다.
    # 마지막 자리까지 정렬이 완료 되었는데 교환횟수가 남은 경우
    # 남은 교환횟수가 짝수이면 종료한다.
    # 남은 교환횟수가 홀수일때
    # 중복되는 숫자가 있으면 종료한다.(두개를 반복하여 교환하면 횟수를 채울 수 있기때문)
    # 중복되는 숫자가 없으면 맨뒤 두개를 교환하고 종료한다.
