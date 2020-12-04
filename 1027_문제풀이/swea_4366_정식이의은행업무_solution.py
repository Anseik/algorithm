import sys
sys.stdin = open('swea_4366_정식이의은행업무.txt')

T = int(input())
for tc in range(1, T + 1):
    binary = list(input())
    tetra = list(input())
    # print(binary, tetra)
    for b in range(len(binary) * 2):
        binary2 = binary[:]
        binary2[b // 2] = str(b % 2)
        # print(binary2)
        bi = ''.join(binary2)
        # print(bi)
        for t in range(len(tetra) * 3):
            tetra2 = tetra[:]
            tetra2[t // 3] = str(t % 3)
            te = ''.join(tetra2)
            if int(bi, 2) == int(te, 3):
                print('#{} {}'.format(tc, int(bi, 2)))
                break

