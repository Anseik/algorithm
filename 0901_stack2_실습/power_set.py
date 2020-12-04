# 멱집합 : 모든 부분집합
# 조합 : 특정 조건을 만족하는 부분집합
# 순열 : 요소들의 순서정렬
arr = [6, 5, 3, 1, 4, 2]
    # [0, 0, 0] # 각 요소가 부분집합에 포함되는지 표시하는 마스킹 배열(bit marking)
N = len(arr)
selected = [0] * N

# idx : 몇번 째 요소의 포함여부를 표시하는 변수
def powerset(idx, sum): # sum 매개변수 추가
    if sum > 5: # 가지치기
        return
    if idx == N: # 이미 모든 요소의 포함여부를 결정했으면
        # print(selected)
        for i in range(N):
            if selected[i] == 1:
                print(arr[i], end=" ")
        print()
        return
    # 현재 상태에서 실행할 수 있는 모든 경우의 수 실행
    # 현재요소 포함
    selected[idx] = 1
    powerset(idx + 1, sum + arr[idx])
    # 현재요소 미포함
    selected[idx] = 0
    powerset(idx + 1, sum)

    # for i in range(2):
    #     selected[idx] = i
    #     powerset(idx + 1)

powerset(0, 0)
# 부분집합의 합이 5이하인 부분집합을 모두 출력하라(백트래킹 이용)
