import sys
sys.stdin = open('특이한자석.txt')

def roll(idx, clock):
    # 시계 방향이면, 제일 뒤쪽 요소 가장 앞으로 붙이기
    if clock == 1:
        tmp = mag[idx].pop()
        mag[idx].insert(0, tmp)
    # 반시계 방향이면 가장 앞쪽요소 뒤로 붙이기
    else:
        tmp = mag[idx].pop(0)
        mag[idx].append(tmp)

# 자석이 영향을 받아서 돌아가는지 확인하는 함수
# 만약에 영향을 받아서 돌아가는 자석이라면, 돌리면 됨
# idx : 확인할 자석의 인덱스
# dir : 검사를 진행하고 있는 방향(왼쪽1, 오른쪽2, 시작3)
# clock : 회전방향 1(시계방향), -1(반시계방향)
def check(idx, clock, dir):
    if idx < 0 or idx >= 4: # 인덱스를 벗어나면 리턴
        return

    # 시작이냐?
    if dir == 3:
        # 왼쪽 진행검사 실행
        check(idx-1, -clock, 1)
        # 오른쪽 검사 실행
        check(idx+1, -clock, 2)
        roll(idx, clock)

    # 왼쪽으로 진행중이었냐
    elif dir == 1:
        if mag[idx][2] != mag[idx + 1][6]:
            check(idx - 1, -clock, 1)
            roll(idx, clock)

    # 오른쪽으로 진행중이었냐
    elif dir == 2:
        if mag[idx][6] != mag[idx - 1][2]:
            check(idx + 1, -clock, 2)
            roll(idx, clock)


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    for i in range(K):
        idx, clock = map(int, input().split())
        # 해당 인덱스에 있는 자석을 돌리면 됨
        # 어떤 자석이 돌아갈지 검사
        check(idx - 1, clock, 3)

    result = 0
    for i in range(4):
        if mag[i][0] == 1:
            result += (2 ** i)

    print('#{} {}'.format(tc, result))