import sys
sys.stdin = open('색칠하기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 전체 영역
    areas = [[0] * 10 for _ in range(10)]
    # print(areas)
    # N개 만큼 영역 생성
    for area in range(N):
        # 각 좌표 값과 컬러값을 언패킹
        r1, c1, r2, c2, color = map(int, input().split())
        # print(r1, c1, r2, c2, color)
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                areas[r][c] += color
        # print(areas)

    cnt = 0
    for r in range(10):
        for c in range(10):
           if areas[r][c] == 3:
               cnt += 1

    # for lst in areas:
    #     print(*lst)

    print('#%d' %tc, cnt)