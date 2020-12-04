import sys
sys.stdin = open('회문.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]
    for k in range(len(words)):
        for j in range(0,len(words[k])-M+1):
            is_pal = True
            for i in range(M//2):
                if words[k][i+j] != words[k][j+M-i-1]:
                    is_pal = False
                    break
            if is_pal == True:
                print('#%d' %tc, words[k][j:j+M])


    for k in range(len(words)):
        for j in range(0,len(words[k])-M+1):
            is_pal = True
            for i in range(M//2):
                if words[i+j][k] != words[j+M-i-1][k]:
                    is_pal = False
                    break
            if is_pal == True:
                result = ""
                for l in range(M):
                    result += words[j+l][k]
                print('#%d' %tc, result)
                print(words)