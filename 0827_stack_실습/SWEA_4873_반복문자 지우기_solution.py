import sys
sys.stdin = open('SWEA_4873_반복문자 지우기_안세익.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    S = []

    for ch in arr:
        # 빈스택이거나 ch와 S[-1] 비교해서 다르면 push
        if not S or ch != S[-1]:
            S.append(ch)
        # 같으면 ch와 S[-1] 버린다.
        else:
            S.pop()

    print(len(S))
