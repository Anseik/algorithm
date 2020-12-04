import sys
import copy
sys.stdin = open('boj_5373_큐빙.txt')

def turn_90(arr): # 시계방향 90도 회전
    N = 3
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = arr[r][c]
    return ret

def turn_270(arr): # 반시계방향 90도 회전
    N = 3
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N - 1 - c][r] = arr[r][c]
    return ret

def switch(plane, clock):
    # 0, 1, 2, 3, 4, 5
    # U, D, F, B, L, R
    tmp = copy.deepcopy(cube)
    if plane == 'U': # r = 0이 회전
        if clock == '+':
            # self
            cube[0] = turn_90(cube[0])
            # F(2) -> L(4) -> B(3) -> R(5) -> F(2)
            cube[4][0], cube[3][0], cube[5][0], cube[2][0] = tmp[2][0], tmp[4][0], tmp[3][0], tmp[5][0]
        elif clock == '-':
            # self
            cube[0] = turn_270(cube[0])
            # F(2) -> R(5) -> B(3) -> L(4) -> F(2)
            cube[5][0], cube[3][0], cube[4][0], cube[2][0] = tmp[2][0], tmp[5][0], tmp[3][0], tmp[4][0]
    elif plane == 'D': # r = 2가 회전
        if clock == '+':
            # self
            cube[1] = turn_90(cube[1])
            # F(2) -> R(5) -> B(3) -> L(4) -> F(2)
            cube[5][2], cube[3][2], cube[4][2], cube[2][2] = tmp[2][2], tmp[5][2], tmp[3][2], tmp[4][2]
        elif clock == '-':
            # self
            cube[1] = turn_270(cube[1])
            # F(2) -> L(4) -> B(3) -> R(5) -> F(2)
            cube[4][2], cube[3][2], cube[5][2], cube[2][2] = tmp[2][2], tmp[4][2], tmp[3][2], tmp[5][2]
    elif plane == 'F':
        if clock == '+':
            # self
            cube[2] = turn_90(cube[2])
            # change
            for c in range(3):
                cube[5][c][0] = tmp[0][2][c]
                cube[1][2][c] = tmp[5][c][0]
                cube[4][c][2] = tmp[1][2][2 - c]
                cube[0][2][c] = tmp[4][2 - c][2]
        elif clock == '-':
            # self
            cube[2] = turn_270(cube[2])
            # change
            for c in range(3):
                cube[4][c][2] = tmp[0][2][2 - c]
                cube[1][2][c] = tmp[4][2 - c][2]
                cube[5][c][0] = tmp[1][2][c]
                cube[0][2][c] = tmp[5][c][0]
    elif plane == 'B':
        if clock == '+':
            # self
            cube[3] = turn_90(cube[3])
            # change
            for c in range(3):
                cube[4][c][0] = tmp[0][0][2 - c]
                cube[1][0][c] = tmp[4][2 - c][0]
                cube[5][c][2] = tmp[1][0][c]
                cube[0][0][c] = tmp[5][c][2]
        elif clock == '-':
            # self
            cube[3] = turn_270(cube[3])
            # change
            for c in range(3):
                cube[5][c][2] = tmp[0][0][c]
                cube[1][0][c] = tmp[5][c][2]
                cube[4][c][0] = tmp[1][0][2 - c]
                cube[0][0][c] = tmp[4][2 - c][0]
    elif plane == 'L':
        if clock == '+':
            # self
            cube[4] = turn_90(cube[4])
            # change
            for c in range(3):
                cube[1][c][2] = tmp[2][2 - c][0]
                cube[3][c][2] = tmp[1][c][2]
                cube[0][c][0] = tmp[3][2 - c][2]
                cube[2][c][0] = tmp[0][c][0]
        elif clock == '-':
            # self
            cube[4] = turn_270(cube[4])
            # change
            for c in range(3):
                cube[0][c][0] = tmp[2][c][0]
                cube[3][c][2] = tmp[0][2 - c][0]
                cube[1][c][2] = tmp[3][c][2]
                cube[2][c][0] = tmp[1][2 - c][2]
    elif plane == 'R':
        if clock == '+':
            # self
            cube[5] = turn_90(cube[5])
            # change
            for c in range(3):
                cube[0][c][2] = tmp[2][c][2]
                cube[3][c][0] = tmp[0][2 - c][2]
                cube[1][c][0] = tmp[3][c][0]
                cube[2][c][2] = tmp[1][2 - c][0]
        elif clock == '-':
            # self
            cube[5] = turn_270(cube[5])
            # change
            for c in range(3):
                cube[1][c][0] = tmp[2][2 - c][2]
                cube[3][c][0] = tmp[1][c][0]
                cube[0][c][2] = tmp[3][2 - c][0]
                cube[2][c][2] = tmp[0][c][2]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    turn = input().split()

    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]
    cube = [U, D, F, B, L, R]

    for i in range(n):
        plane = turn[i][0]
        clock = turn[i][1]
        switch(plane, clock)

    for i in range(3):
        for j in range(3):
            print(cube[0][i][j], end="")
        print()