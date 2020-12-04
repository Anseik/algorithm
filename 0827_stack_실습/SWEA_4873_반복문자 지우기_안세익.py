import sys
sys.stdin = open('SWEA_4873_반복문자 지우기_안세익.txt')

# 연속해서 나오는지 체크
def del_repeat(target):
    for i in range(0, len(target) - 1):
        if target[i] == target[i + 1]:
            target = target[:i] + target[i+2:]
            return del_repeat(target) # 반복을 제거한 문자열을 target으로 다시 함수 호출

    return len(target)

T = int(input())
for tc in range(1, T+1):
    target = input()
    result = del_repeat(target)

    print("#{} {}".format(tc, result))