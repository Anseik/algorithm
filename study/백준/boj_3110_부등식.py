import sys
from math import ceil, floor
sys.stdin = open('boj_3110_부등식.txt')

B, C, D = map(int, input().split())
A1, A2 = map(int, input().split())
E1, E2 = map(int, input().split())

# 물음표 자리에 들어갈 양의 정수 : x, y, z
# y값이 정해지면 x값과 z값은 정해진다.
# y값의 범위를 확인해서 for문을 돌리자
min_y = floor((A1 * C) / A2) + 1
max_y = ceil((E1 * C) / E2) - 1

# y값이 정해지기 전에 알 수 있는 x의 최소값과 z의 최대값은 미리 구해놓는다.
min_x = floor((A1 * B) / A2) + 1
max_z = ceil((E1 * D) / E2) - 1

cnt = 0
for y in range(min_y, max_y + 1):
    # y값이 정해지면 그에 따라 x와 z의 범위가 결정된다.
    max_x = ceil((y * B) / C) - 1
    min_z = floor((y * D) / C) + 1
    # y값에 따른 x와 z의 개수를 곱해서 cnt에 누적한다.
    cnt += (max_x - min_x + 1) * (max_z - min_z + 1)

print(cnt)