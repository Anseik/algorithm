T = 10
for tc in range(1, T+1):
    t = int(input())
    N = 100
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
    max = 0
    for row in matrix:
        for i in range(N):
            for a in range(1, N-i+1):
                #print(len(row[i:i+a]))
                if isPalindrome(row[i:i+a], 0, len(row[i:i+a])-1):
                    cnt = len(row[i:i+a])
                    if cnt > max:
                        max = cnt

    #열 확인
    for i in range(N):
        column = [mat[i] for mat in matrix]
        column = "".join(column)
        for i in range(N):
            for a in range(1, N - i + 1):
                # print(len(row[i:i+a]))
                if isPalindrome(column[i:i + a], 0, len(column[i:i + a]) - 1):
                    cnt = len(column[i:i + a])
                    if cnt > max:
                        max = cnt

    # 최댓값 추출
    print('#{} {}'.format(tc, max))
