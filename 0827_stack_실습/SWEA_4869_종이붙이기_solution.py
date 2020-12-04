import sys
sys.stdin = open('종이붙이기.txt')

# 재귀 호출 기본형
def f(n): # n : 문제의 크기(식별값)
    # 기저 사례
    if n == 1: return 1
    if n == 2: return 3

    return f(n - 1) + f(n - 2) * 2


# memoization을 이용한 재귀 1
def f2(n): # n : 문제의 크기(식별값)
    # 기저 사례
    if n == 1: return 1
    if n == 2: return 3

    # 일반사례
    if memo[n]: return memo[n]

    memo[n] = f2(n - 1) + f2(n - 2) * 2

    return memo[n]


# memoization을 이용한 재귀 2
def f3(n): # n : 문제의 크기(식별값)
    if n > 2 and len(memo2) <= n:
        memo2.append(f3(n - 1) + f3(n - 2) * 2)

    return memo2[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    memo = [0] * (N + 1) # 초기값 0 --> 이 문제의 답을 아직 구하지 않음.
    memo2 = [0, 1, 3]

    # 반복을 통한 재귀
    memo[1], memo[2] = 1, 3
    for i in range(3, N+1): # i --> 문제의 크기를 나타내는 값
        memo[i] = memo[i - 1] + memo[i - 2] * 2

    print(memo[N])
    # print(f2(N))
