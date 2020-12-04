import sys
sys.stdin = open('전기버스.txt')

T = int(input())
for tc in range(1, T+1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점 번호
    # M : 충전기가 설치된 정류장 개수
    K, N, M = map(int, input().split())
    power = list(map(int, input().split()))
    # print(K, N, M)
    # print(power)

    line = [0] * (N+1)
    for i in range(M):
        line[power[i]] += 1

    # print(line)

    # 버스의 위치를 저장하는 변수
    position = 0
    # 충전 횟수를 카운트하는 변수
    cnt = 0

    while position < N:
        for j in range(K, 0, -1):
            if (position+j) >= N:
                position = N
                break
            elif line[position+j] == 1:
                cnt += 1
                position += j
                break

        else:
            cnt = 0
            break

    print("#{} {}".format(tc, cnt))
