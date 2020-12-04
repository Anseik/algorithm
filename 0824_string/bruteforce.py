p = "is"
t = "This is a book~!"
M = len(p)
N = len(t)

def bruteforce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i - M
    else:
        return -1

print(bruteforce(p, t))