# 표준입력을 받아옴: 기본 설정 >> 콘솔키보드입력
# 기본 입력을 >> 파일에서 읽어오도록 변경
# 변경을 하려면 sys

import sys
sys.stdin = open('input.txt')
# a = int(input()) # 'input.txt파일을 한줄씩 읽어온다 / 문자열이기때문에 숫자료 형변환
# b = list(map(int, input().split())) # 입력받은 문자열은 띄어쓰기를 기준으로 리스트로 만들고 map함수를 사용해서 int로 형변환
# c = int(input())
# d = list(map(int, input().split()))
#
# print(a)
# print(b)
# print(c)
# print(d)
num = 0
for i in range(10):
    a = int(input())
    b = list(map(int, input().split()))
    num += 1
    # print(a, '//', b)

    cnt = 0
    for i in range(2, a):
        if b[i] > b[i-1] and b[i] > b[i-2] and b[i] > b[i+1] and b[i] > b[i+2]:
            cnt += (b[i] - max(b[i-2], b[i-1], b[i+1], b[i+2]))


    result = '#' + str(num) + ' ' + str(cnt)
    print(result)