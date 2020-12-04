def quick_sort(arr, left, right):
    # 시작과 끝점을 기준으로 작업하는데 시작점이 끝점보다 작을때만 실행
    if left < right:
        pivot = lomuto_partition(arr, left, right)
        # 피벗을 기준으로 큰값과, 작은값으로 정렬(partition)
        # 왼쪽 부분집합 정렬 실행
        quick_sort(arr, left, pivot - 1)
        # 오른쪽 부분집합 정렬 실행
        quick_sort(arr, pivot + 1, right)


def hoare_partition(arr, left, right):
    i = left
    j = right
    pivot = arr[left]

    # i가 j보다 작거나 같을 때까지 계속 반복(left 와 right가 역전되면 수행 X)
    while i <= j:
        # i는 증가하면서 pivot보다 큰 값을 찾고
        while arr[i] <= pivot:
            i += 1
        # j는 감소하면서 pivot보다 작은 값을 찾는다.
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗보다 작은값 중 제일 뒤에 위치한 arr[j]와 pivot의 위치를 바꿔준다.
    arr[left], arr[j] = arr[j], arr[left]
    return j



# i는 피봇보다 큰값을 가르키고 있고
# j는 피봇보다 작은 값을 가르킨다.
def lomuto_partition(arr, left, right):
    # 오른쪽을 피벗으로 설정
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        # arr[j]가 pivot보다 작은 값을 찾는다.
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 스왑을 하고나면 i가 가리키는 위치는 pivot보다 작은 값의 마지막 인덱스
    # i + 1의 위치에 피벗을 둔다.
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1



arr = [4, 3, 2, 1, 7, 5, 5, 2]
quick_sort(arr, 0, len(arr)-1)
print(arr)