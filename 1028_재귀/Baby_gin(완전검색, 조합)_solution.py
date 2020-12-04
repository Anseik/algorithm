"""
124783
667767
054060
101123
"""

arr = ['124783', '667767', '054060', '101123']

# baby-jin 완전탐색으로 풀기
# 조합으로 풀어보기, 6가지 중에 3가지 숫자를 선택 후 정렬
# 1, 2, 3, 4, 5, 6 / 해당 요소를 포함하는 경우와 하지 않는 경우를 모두 탐색
N = 6
K = 3
selected = [0] * N
def comb(selected, idx, cnt):
    if cnt == K: # 조합에 포함되는 모든 요소를 선택했다.
        print(selected)
        return
    if idx == N: # 모든 인덱스의 포함여부를 결정한 경우
        return

    # idx에 해당하는 요소를 조합에 포함할지 안할지 결정
    selected[idx] = 1
    comb(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    comb(selected, idx + 1, cnt)

# 2그룹으로 구분하기만 되므로 중복을 제거하기 위해 첫번째 요소를 선택했다고 가정하고 가능한 조합을 구한다.
selected[0] = 1
comb(selected, 1, 1)
