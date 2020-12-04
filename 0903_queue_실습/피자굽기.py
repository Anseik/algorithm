import sys
sys.stdin = open('피자굽기.txt')

T = int(input())
for tc in range(1, T+1):
    # 화덕의 크기 N, 피자 개수 M
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    # print(N, M)
    # print(C)

    check = [] # 피자의 치즈량과 번호를 가지고 있는 이차원 배열을 만든다.
    number = 0
    for i in range(M):
        number += 1
        check.append([C[i], number]) # 치즈량과 번호를 요소로 가지는 리스트를 check에 추가한다.
    # print(check)

    # 화덕 생성 및 초기화
    oven = [0] * N
    for i in range(N):
        oven[i] = check.pop(0)
    # print(oven)

    # 오븐이 한 바퀴 돈다.(초기화했을때랑 같은 상태라 굳이 필요는 없지만 논리상 필요하다.)
    for j in range(N):
        oven.append(oven.pop(0))
    # print(oven)

    while True: # 오븐이 한 바퀴 돌고나서는 입구에 오는 피자의 치즈량을 확인하고
        # 치즈가 다 녹으면 빼고 다음 피자를 넣은 것을 피자가 하나 남을때까지 반복한다.

        oven[0][0] = oven[0][0] // 2  # 입구에 있는 피자의 안 녹은 치즈량이 반으로 줄어든다.
        if oven[0][0] == 0: # 치즈가 다 녹으면
            oven[0] = [0, 0] # 해당 자리를 초기화 한다. 즉, 피자를 꺼낸다.
            if len(check) != 0: # 남은 피자가 있을 때
                oven[0] = check.pop(0) # 남은 피자를 넣어준다.

        # 현재 오븐에 들어있는 피자의 개수확인
        cnt = 0
        for i in range(N):
            if oven[i][0] != 0:
                cnt += 1

        # 현재 오븐에 들어있는 피자의 개수가 1개면 반복문 종료
        if cnt == 1:
            break

        # 아니면 계속 회전
        oven.append(oven.pop(0))


    # 피자가 하나 남았을 때 오븐을 확인하며 몇번째 피자가 남아 있는지 출력한다.
    for i in range(N):
        if oven[i][0] != 0:
            print("#{} {}".format(tc, oven[i][1]))