import sys
sys.stdin = open('boj_1365_꼬인전깃줄.txt')

N = int(input())
power_li = list(map(int, input().split()))
lis = [0] * (N + 1)
final_idx = 0 # lis의 마지막 숫자를 가르키는 인덱스
power_idx = 1 # power_li를 순회하는 인덱스
cnt = 0 # lis의 길이
lis[final_idx] = power_li[0]


def lower_bound(start, end, target):
    while start < end:
        middle = (start + end) // 2
        if lis[middle] < target:
            start = middle + 1
        else:
            end = middle
    return end

while power_idx < N:
    # lis의 마지막 숫자보다 이번에 들어갈 숫자가 클때
    if lis[final_idx] < power_li[power_idx]:
        final_idx += 1
        lis[final_idx] = power_li[power_idx]

    # lis의 마지막 숫자보다 이번에 들어갈 숫자가 작을때
    # 이번에 들어갈 숫자가 어디에 들어가야하는지 위치를 찾아야한다.
    else:
        pos = lower_bound(0, final_idx, power_li[power_idx])
        lis[pos] = power_li[power_idx]
        cnt += 1

    power_idx += 1

print(cnt)