import sys

for tc in range(int(sys.stdin.readline().rstrip())):
    N = int(sys.stdin.readline().rstrip())

    li = [sys.stdin.readline().rstrip() for _ in range(N)]
    li.sort()
    # print(li)

    result = 'YES'
    for i in range(1, N):
        if li[i].startswith(li[i - 1]):
            result = 'NO'
            break

    print(result)
