import sys

sys.stdin = open('boj_1365_꼬인전깃줄.txt')


# 가장 긴 증가하는 부분수열을 찾자
def comb(sub_arr, idx):
    global lis
    # sub_arr의 길이에 남은 요소의 길이를 모두 더해도 lis보다 작으면 리턴
    if len(sub_arr) + (N - 1) - idx < lis:
        return
    if idx == N:
        lis = max(lis, len(sub_arr))
        return
    if len(sub_arr) == 0:
        select[idx] = 1
        comb(sub_arr + [arr[idx]], idx + 1)
    else:
        if sub_arr[-1] < arr[idx]:
            select[idx] = 1
            comb(sub_arr + [arr[idx]], idx + 1)

    select[idx] = 0
    comb(sub_arr, idx + 1)


N = int(input())
arr = list(map(int, input().split()))
select = [0] * N
lis = 0
comb([], 0)
ans = N - lis
print(ans)
