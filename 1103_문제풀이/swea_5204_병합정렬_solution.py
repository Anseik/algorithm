# 정렬하고자 하는 배열을 더 이상 나눌 수 없을때까지 절반으로 나눈다.
# 병합 : 각각의 배열을 앞쪽부터 순회하면서, 작은 값부터 새로운 배열에 복사

import sys
sys.stdin = open('swea_5204_병합정렬_solution.txt')

def merge_sort(arr):
    # 나누기(길이가 1보다 클때만)
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    # 왼쪽부분 재귀 호출
    left = merge_sort(arr[:mid])
    # 오른쪽 부분 재귀 호출
    right = merge_sort(arr[mid:])
    # 병합
    return merge(left, right)


def merge(left, right): # left와 right를 병합
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = list()
    # left와 right를 앞쪽부터 비교하면서 작은 값을 result에 추가하기
    i = j = 0
    while i < len(left) or j < len(right): # 둘 중에 하나라도 복사할 요소가 남아있으면
        # 왼쪽, 오른쪽 다 남아있을때
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # 왼쪽만 남았거나
        elif i < len(left):
            result.append(left[i])
            i += 1
        # 오른쪽만 남았거나
        elif j < len(right):
            result.append(right[j])
            j += 1

    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr= list(map(int, input().split()))
    cnt = 0
    L = merge_sort(arr)
    print('#{} {} {}'.format(tc, L[N//2], cnt))