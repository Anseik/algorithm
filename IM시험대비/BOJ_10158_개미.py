import sys
sys.stdin = open('BOJ_10158_개미.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
# print(w, h)
# print(p, q)
# print(t)

board = [[0] * (w + 1) for _ in range(h + 1)]
print(board)

board[q][p] = 1
print(board)