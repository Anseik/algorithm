import sys
sys.stdin = open('swea_1244_최대상금.txt')


def perm(idx, cnt):
    global find_max, max_case, change

    if find_max == True: # 이미 최대값을 찾았으면 더 이상 순열을 생성하지 않는다.
        return

    # 순열을 생성하던 중 최대값이 나오면 더 이상 순열을 생성하지 않아도 된다.
    if numbers == max_sort:
        find_max = True
        change = cnt # 최대값을 찾을 때까지 교환한 횟수를 change에 저장하고 함수종료 후 남은 교환 횟수를 계산해 후처리한다.
        return

    # 교환횟수를 모두 채운경우
    if cnt == switch:
        tmp = int(''.join(numbers))
        if max_case < tmp: # switch번의 교환으로 만들 수 있는 최적해
            max_case = tmp
        return

    if idx == N:
        return

    for i in range(idx + 1, N):
        if numbers[i] > numbers[idx]: # 뒤에 자신보다 큰 숫자가 있는 경우에만 교환한다.
            numbers[idx], numbers[i] = numbers[i], numbers[idx]
            perm(idx + 1, cnt + 1)
            numbers[idx], numbers[i] = numbers[i], numbers[idx]
    else: # 교환할게 없으면 다음 숫자로 넘어간다.
        perm(idx + 1, cnt)


T = int(input())
for tc in range(1, T + 1):
    numbers, switch = input().split()
    numbers = list(map(str, numbers))
    switch = int(switch)
    N = len(numbers)
    # print(numbers, switch)

    max_sort = sorted(numbers, reverse=True) # 내림차순 정렬해서 최대값을 찾아놓고 perm함수를 실행한다.
    max_num = int(''.join(max_sort))
    # print(max_num)

    find_max = False # 최대값을 찾았는지 여부
    change = 0 # 최대값을 찾을 때까지 교환한 횟수
    max_case = 0 # switch번의 교환으로 만들 수 있는 최적해
    perm(0, 0)

    if find_max: # 최대값을 찾은 경우
        rest = switch - change # 남은 교환 횟수
        if rest % 2 == 0:  # 남은 교환횟수가 짝수일때는 그냥 출력
            print('#{} {}'.format(tc, max_num))
        else:  # 남은 교환횟수가 홀수일때
            # 중복이 있으면 그냥 출력
            for k in range(N):
                if numbers.count(numbers[k]) >= 2:
                    print('#{} {}'.format(tc, max_num))
                    break
            else: # 중복이 없으면 맨 뒷자리 2개를 교환해서 출력
                max_sort[-1], max_sort[-2] = max_sort[-2], max_sort[-1]
                ans = int(''.join(max_sort))
                print('#{} {}'.format(tc, ans))

    else: # switch번만큼 교환을 한 경우 최적해를 출력한다.
        print('#{} {}'.format(tc, max_case))

    # 정렬했을때 만들 수 있는 최대수가 무엇인지 찾아놓는다.
    # 순열을 생성하던 도중 최대수와 같아지면 최대수를 찾을 때까지 교환한 횟수를 저장하고 더 이상 순열을 생성하지 않는다.
    # 최대수와 같아지지 않으면 switch번 교환해서 만들 수 있는 가장 큰 수(최적해)를 찾는다.
    # 교환 횟수가 남았을때 짝수번 남았으면 최대수를 출력
    # 홀수번 남았으면 중복되는 수가 있는지 확인
    # 중복이 있으면 그냥 출력
    # 중복이 없으면 제일뒤 두개를 교환해서 출력
