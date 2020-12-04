import sys
sys.stdin = open('신뢰.txt')

def pressbtn():
    pass

T = int(input())
for tc in range(1, T + 1):
    Obtn = [0] * 101
    Bbtn = [0] * 101

    arr = input().split()
    # print(arr)

    N = int(arr.pop(0))
    # print(N)

    button = []
    Otarget = 0
    Btarget = 0
    for i in range(N):
        button.append((arr[2 * i], int(arr[2 * i + 1])))
        if arr[2 * i] == 'O':
            Otarget += 1
            Obtn[int(arr[2 * i + 1])] = 1
        else:
            Btarget += 1
            Bbtn[int(arr[2 * i + 1])] = 1

    print(button)
    # print(Obtn)
    # print(Bbtn)
    # print(Otarget)
    # print(Btarget)