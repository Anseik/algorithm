# 전치행렬 이용 : 전치 후 가로검사하면 세로검사를 하는 것과 동일!
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# test = list(zip(*arr))
# print(test)


import sys
sys.stdin = open('회문2.txt')

def check_pal(M): # 회문의 길이를 입력받아서 해당길이의 회문이 있는지 없는지 판단
    global N
    for i in range(N):
        for j in range(N-M+1):
            # 회문검사
            # 회문검사 대상 추출
            tmp1 = board[i][j:j+M] # 가로회문 검사대상
            tmp2 = zboard[i][j:j+M] # 세로회문 검사대상
            if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
                return True
    return False


T = 10
N = 100
for x in range(T):
    tc = int(input())
    board = [input() for _ in range(N)]
    zboard = list(zip(*board))
    # 가로에 회문이 있는지 검사
    # 전치행렬의 가로 검사를 하면, 원래 행렬의 세로 검사와 같다.
    # 가장 긴 회문을 찾으면 되니까, 긴 것부터 검사를 하면된다.
    result = 0
    for i in range(N, 0, -1): # 가장 긴 회문의 길이는 N 가장 짧은 회문의 길이는 1
        if check_pal(i):
            result = i
            break

    print("#{} {}".format(tc, result))