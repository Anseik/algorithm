# 퀵 정렬
# 피벗을 정하고 피벗보다 작은값을 앞쪽으로
# 피벗보다 큰값을 뒤쪽으로 보내면, 피벗의 위치가 결정됨
# 나누어진 부분을 다시 피벗을 기준으로 정리하면 반복하여 피벗의 위치가 결정되고
# 끝까지 진행하면 정렬이 완료된다.
# 퀵정렬의 두 가지 작업
# 파티션 : 전체를 두 부분으로 나누는 작업
# 퀵정렬 : 나누어진 두 부분을 각각 다시 퀵정렬

def partition(arr, start, end):
    # 피벗 선택하고, 제일 앞쪽 값을 피벗으로 설정(피벗은 달라질 수 있다.)
    pivot = arr[start]
    # 피벗보다 작으면 앞쪽으로, 크면 뒤쪽으로 보내기
    # [6][5][7][1][8][3][6][4][9]
       # left               # right
    left = start + 1 # 피벗은 검사할 필요없으므로 +1한다.
    right = end
    while left <= right: # left가 right보다 커지면 종료
        # left가 오른쪽으로 이동하며, 피벗보다 큰 값을 찾기
        while left <= right and arr[left] <= pivot:
            left += 1
        # right가 왼쪽으로 이동하며, 피벗보다 작은값을 찾기
        while left <= right and arr[right] > pivot:
            right -= 1
        # 각각 pivot보다 큰값과 작은값을 찾았으면, 위치교환
        if left < right: #
            arr[left], arr[right] = arr[right], arr[left]
    # 피벗을 제외하고 피벗보다 작으면 왼쪽, 피벗보다 크면 오른쪽에 위치
    # right가 가르키고 있는 값은 피벗보다 작은 값 중 가장 오른쪽에 있는 값
    # (pivot ...... right left......)
    # right와 피벗의 위치를 바꾸면 pivot을 기준으로 왼쪽에는 작은값이 오른쪽에는 큰 값이 위치한다.
    arr[start], arr[right] = arr[right], arr[start]

    return right


def quick_sort(arr, start, end):
    if start < end:
        # 파티션을 실행하고
        # 파티션으로 나누어진 부분을 각각 다시 퀵 소트
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return

target = [3, 5, 1, 2, 7, 4, 6]
quick_sort(target, 0, len(target)-1)
print(target)

