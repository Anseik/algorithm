"""
124783
667767
054060
101123
"""

target = list(map(int, input()))
# print(target)
N = len(target)
result = False
def perm(idx):
    global result
    if idx == N:
        cnt = 0
        for j in range(0, N, 3):
            # triplet인 경우 검사
            if target[j] == target[j + 1] and target[j + 1] == target[j + 2]:
                cnt += 1
            # run인 경우 검사
            if target[j + 1] - target[j] == 1 and target[j + 2] - target[j + 1] == 1:
                cnt += 1
        if cnt == 2:
            result = True
        return

    for i in range(idx, N):
        target[idx], target[i] = target[i], target[idx]
        perm(idx + 1)
        target[idx], target[i] = target[i], target[idx]

perm(0)

if result:
    print('Baby-gin입니다.')
else:
    print('Baby-gin이 아닙니다.')