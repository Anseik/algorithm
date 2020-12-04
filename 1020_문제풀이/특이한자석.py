import sys
sys.stdin = open('특이한자석.txt')

def rotation(num, dir, chain):
    if num == 1: # 1번 자석을 처음 회전 시키는 경우
        if dir == 1: # 시계 방향
            tmp = M1.pop(7)
            M1.insert(0, tmp)
        else: # 반시계 방향
            tmp = M1.pop(0)
            M1.insert(7, tmp)
        if chain[0] == 1: # 1, 2번이 연결되어 있으면
            dir2 = -dir
            if dir2 == 1:  # 시계 방향
                tmp = M2.pop(7)
                M2.insert(0, tmp)
            else:  # 반시계 방향
                tmp = M2.pop(0)
                M2.insert(7, tmp)
            if chain[1] == 1: # 1, 2, 3번이 연결되어 있으면
                dir3 = -dir2
                if dir3 == 1:  # 시계 방향
                    tmp = M3.pop(7)
                    M3.insert(0, tmp)
                else:  # 반시계 방향
                    tmp = M3.pop(0)
                    M3.insert(7, tmp)
                if chain[2] == 1: # 1, 2, 3, 4번이 연결되어 있으면
                    dir4 = -dir3
                    if dir4 == 1:  # 시계 방향
                        tmp = M4.pop(7)
                        M4.insert(0, tmp)
                    else:  # 반시계 방향
                        tmp = M4.pop(0)
                        M4.insert(7, tmp)

    elif num == 2: # 2번 자석을 처음 회전 시키는 경우
        if dir == 1: # 시계 방향
            tmp = M2.pop(7)
            M2.insert(0, tmp)
        else: # 반시계 방향
            tmp = M2.pop(0)
            M2.insert(7, tmp)
        if chain[0] == 1: # 2, 1번이 연결되어 있는 경우
            dir1 = -dir
            if dir1 == 1:  # 시계 방향
                tmp = M1.pop(7)
                M1.insert(0, tmp)
            else:  # 반시계 방향
                tmp = M1.pop(0)
                M1.insert(7, tmp)
        if chain[1] == 1: # 2, 3번이 연결되어 있는경우
            dir3 = -dir
            if dir3 == 1:  # 시계 방향
                tmp = M3.pop(7)
                M3.insert(0, tmp)
            else:  # 반시계 방향
                tmp = M3.pop(0)
                M3.insert(7, tmp)
            if chain[2] == 1: # 2, 3, 4번이 연결되어 있는 경우
                dir4 = -dir3
                if dir4 == 1:  # 시계 방향
                    tmp = M4.pop(7)
                    M4.insert(0, tmp)
                else:  # 반시계 방향
                    tmp = M4.pop(0)
                    M4.insert(7, tmp)

    elif num == 3: # 3번 자석을 처음 회전 시키는 경우
        if dir == 1: # 시계 방향
            tmp = M3.pop(7)
            M3.insert(0, tmp)
        else: # 반시계 방향
            tmp = M3.pop(0)
            M3.insert(7, tmp)
        if chain[2] == 1: # 3, 4번이 연결되어 있는 경우
            dir4 = -dir
            if dir4 == 1:  # 시계 방향
                tmp = M4.pop(7)
                M4.insert(0, tmp)
            else:  # 반시계 방향
                tmp = M4.pop(0)
                M4.insert(7, tmp)
        if chain[1] == 1: # 3, 2번이 연결되어 있는 경우
            dir2 = -dir
            if dir2 == 1:  # 시계 방향
                tmp = M2.pop(7)
                M2.insert(0, tmp)
            else:  # 반시계 방향
                tmp = M2.pop(0)
                M2.insert(7, tmp)
            if chain[0] == 1: # 3, 2, 1번이 연결되어 있는 경우
                dir1 = -dir2
                if dir1 == 1:  # 시계 방향
                    tmp = M1.pop(7)
                    M1.insert(0, tmp)
                else:  # 반시계 방향
                    tmp = M1.pop(0)
                    M1.insert(7, tmp)

    else: # 4번 자석을 처음 회전 시키는 경우
        if dir == 1: # 시계 방향
            tmp = M4.pop(7)
            M4.insert(0, tmp)
        else: # 반시계 방향
            tmp = M4.pop(0)
            M4.insert(7, tmp)
        if chain[2] == 1: # 4, 3번이 연결되어 있는 경우
            dir3 = -dir
            if dir3 == 1:  # 시계 방향
                tmp = M3.pop(7)
                M3.insert(0, tmp)
            else:  # 반시계 방향
                tmp = M3.pop(0)
                M3.insert(7, tmp)
            if chain[1] == 1: # 4, 3, 2번이 연결되어 있는 경우
                dir2 = -dir3
                if dir2 == 1:  # 시계 방향
                    tmp = M2.pop(7)
                    M2.insert(0, tmp)
                else:  # 반시계 방향
                    tmp = M2.pop(0)
                    M2.insert(7, tmp)
                if chain[0] == 1: # 4, 3, 2, 1번이 연결되어 있는 경우
                    dir1 = -dir2
                    if dir1 == 1:  # 시계 방향
                        tmp = M1.pop(7)
                        M1.insert(0, tmp)
                    else:  # 반시계 방향
                        tmp = M1.pop(0)
                        M1.insert(7, tmp)

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    M1 = list(map(int, input().split()))
    M2 = list(map(int, input().split()))
    M3 = list(map(int, input().split()))
    M4 = list(map(int, input().split()))
    # print(M1, M2, M3, M4)

    # rots = []
    # for i in range(K):
    #     rots.append(list(map(int, input().split())))
    # print(rots)

    # 0 1 2 3 4 5 6 7
    # 연결된 부분
    # 1번 자석의 idx 2와 2번 자석의 idx 6
    # 2번 자석의 idx 2와 3번 자석의 idx 6 / 2번 자석의 idx 6과 1번 자석의 idx 2
    # 3번 자석의 idx 2와 4번 자석의 idx 6 / 3번 자석의 idx 6과 2번 자석의 idx 2
    # 4번 자석의 idx 6과 3번 자석의 idx 2

    # 시계방향 회전
    # 마지막 요소를 pop해서 맨 앞에 insert
    # 반시계방향 회전
    # 첫 요소를 pop해서 마지막에 append

    for _ in range(K):
        # 연결정보
        chain = [0] * 3
        if M1[2] != M2[6]:
            chain[0] = 1
        if M2[2] != M3[6]:
            chain[1] = 1
        if M3[2] != M4[6]:
            chain[2] = 1
        print(chain)

        num, dir = map(int, input().split())
        # print(num, dir)

        rotation(num, dir, chain)

    result = (M1[0] * 1) + (M2[0] * 2) + (M3[0] * 4) + (M4[0] * 8)
    print("#{} {}".format(tc, result))