import sys
sys.stdin = open('문자열 압축.txt')


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1): # 가능한 단위는 1 ~ len(s) // 2까지이다.
        com = list() # 단위 i로 압축했을때 문자열에 들어갈 요소의 리스트
        x = s
        while len(x):
            cnt = 1
            for k in range(len(x) // i + 1): # 비교횟수, 마지막에 남은 문자열을 리스트에 포함하기 위해 +1 했다.
                if x[i * k : i * (k+1)] == x[i * (k+1) : i * (k+2)]: # 해당 단위만큼 슬라이싱해 다음 단위 문자열과 비교
                    cnt += 1
                else:
                    if k != 0: # 최초 비교가 아니면 for문 밖으로 나가 바로 if문을 실행
                        break
                    if k == 0: # 최초 비교이면 즉, 압축할 것이 없으면
                        com.append(x[i * k : i * (k+1)]) # com에 해당 문자열을 추가하고
                        x = x.replace(x[i * k : i * (k+1)], "", cnt) # x에서는 제거한다.
                        break
            if cnt > 1: # for문을 돌았을때 cnt가 1보다 크면 즉, 압축할 수 있는 것이 있었으면
                com.append(str(cnt)) # join하여 다시 문자열로 만들기 위해 str로 형변환
                com.append(x[i * k : i * (k+1)]) # com에 해당 문자열을 추가하고
                x = x.replace(x[i * k : i * (k+1)], "", cnt) # x에서는 제거한다.

        tmp = "".join(com) # 완성된 com을 다시 문자열로 만든다.
        if len(tmp) < answer: # 압축한 결과가 answer의 길이보다 짧으면
            answer = len(tmp) # answer에 단위 i로 압축한 결과의 길이를 저장한다.

    return answer # 단위 i ~ len(s)//2까지 모두 실행하였을때 즉, 모든 압축가능한 경우의 수를 탐색하였을때 가장 짧은 압축 길이를 반환


T = int(input())
for tc in range(1, T+1):
    s = input()
    answer = solution(s)

    print("#{} {}".format(tc, answer))