# 첫 번째 줄에는 테스트 케이스 개수 T
# T개의 테스트 케이스가 주어진다.
# input() : 문자열 한 줄을 입력받음. 결과 >> 문자열
# 문자열이 필요한게 아니라 숫자가 필요 >>
import sys
sys.stdin = open('test.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # board = list() # 이차원 배열 선언
    # for n in range(N):
    #     list(map(int, board.append(input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]

    print(board)