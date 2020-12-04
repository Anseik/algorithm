import sys
sys.stdin = open('boj_1524_세준세비.txt')

T = int(input())
for tc in range(T):
    empty = input()
    N, M = map(int, input().split())
    Sarmy = sys.stdin.readline().split()
    Barmy = sys.stdin.readline().split()
    # print(N, M)
    # print(Sarmy)
    # print(Barmy)

    while True:
        Smin = min(Sarmy)
        Bmin = min(Barmy)
        # print(Smin,Bmin)
        if Smin < Bmin:
            Sarmy.pop(Sarmy.index(Smin))
        else:
            Barmy.pop(Barmy.index(Bmin))

        if len(Sarmy) != 0 and len(Barmy) == 0:
            print('S')
            break
        elif len(Sarmy) == 0 and len(Barmy) != 0:
            print('B')
            break

