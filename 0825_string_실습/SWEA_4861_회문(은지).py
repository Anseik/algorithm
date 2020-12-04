T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]  # N X N 행렬

    # 팰린드롬 판별하는 함수
    def isPalindrome(string, start, end):
        if start == end:  # 문자가 하나 일 때
            return True
        elif start + 1 == end:  # 문자가 2개 일 때
            if string[start] == string[end]:  # AA BB CC 이런거
                return True
            else:
                return False
        else:  # 문자가 3개 이상일 때
            if string[start] == string[end]:
                return isPalindrome(string, start + 1, end - 1)
            else:
                return False


    #행 확인
    for row in matrix:
        for i in range(N-M+1):
            if isPalindrome(row[i:i+M], 0, M-1):
                print('#{} {}'.format(tc, row[i:i+M]))
    #열 확인
    for i in range(N):
        column = [mat[i] for mat in matrix]
        column = "".join(column)
        for i in range(N-M+1):
            if isPalindrome(column[i:i + M], 0, M - 1):
                print('#{} {}'.format(tc, column[i:i + M]))
