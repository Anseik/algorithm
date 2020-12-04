import sys
sys.stdin = open('특이한자석.txt')

def rotation(num, dir, chain):
    # 자기자신을 포함한 오른쪽 연결정보 확인
    dr = dir
    for i in range(num, 5):
        target = mags[i]
        if dr == 1:  # 시계 방향
            tmp = target.pop(7)
            target.insert(0, tmp)
        else:  # 반시계 방향
            tmp = target.pop(0)
            target.insert(7, tmp)
        if chain[i] == 0:
            break
        dr *= -1


    # 왼쪽 연결정보 확인
    dl = -dir
    for j in range(num - 1, 0, -1):
        if chain[j] == 0:
            break
        target = mags[j]
        if dl == 1:  # 시계 방향
            tmp = target.pop(7)
            target.insert(0, tmp)
        else:  # 반시계 방향
            tmp = target.pop(0)
            target.insert(7, tmp)
        dl *= -1

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    mags = [0]
    for _ in range(4):
        mags.append(list(map(int, input().split())))
    # print(mags)

    # 연결정보

    for i in range(K):
        chain = [0] * 5  # 초기화, 0번, 4번인덱스는 미사용
        for n in range(1, 4):
            if mags[n][2] != mags[n+1][6]:
                chain[n] = 1
        # print(chain)

        num, dir = map(int, input().split())
        # print(num, dir)
        rotation(num, dir, chain)

    result = (mags[1][0] * 1) + (mags[2][0] * 2) + (mags[3][0] * 4) + (mags[4][0] * 8)
    print("#{} {}".format(tc, result))