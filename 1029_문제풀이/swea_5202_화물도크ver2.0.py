import sys
sys.stdin = open('swea_5202_화물도크.txt')


T = int(input())
for tc in range(1, T + 1):
    # 신청서의 개수
    N = int(input())
    # [시작, 종료]
    apl = []
    for i in range(N):
        apl.append(list(map(int, input().split())))
    #print(apl)

    apl = sorted(apl, key = lambda x : x[1])
    # print(apl)

    cnt = e = 0
    for i in range(N):
        # 이번 신청서의 시작 시간이 이전 신청서의 종료시간보다 같거나 클때 가능
        if apl[i][0] >= e:
            cnt += 1 # 그 신청서를 처리하고
            e = apl[i][1] # 종료시간을 최신화 한다.

    print('#{} {}'.format(tc, cnt))