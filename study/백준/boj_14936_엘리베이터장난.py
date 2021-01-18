import sys
sys.stdin = open('boj_14936_엘리베이터장난.txt')

N, m = map(int, input().split())

# t1 : 모든 버튼을 다 누르는데 걸리는 시간
# t2 : 짝수 버튼만 다 누르는데 걸리는 시간
# t3 : 홀수 버튼만 다 누르는데 걸리는 시간
# t4 : 3k + 1번 버튼만 다 누르는데 걸리는 시간

t1 = N
t2 = N // 2
t3 = (N + 1) // 2
t4 = (N - 1) // 3 + 1

