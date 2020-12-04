def search(t, p):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        for j in range(M):
            if p[j] != t[i+j]:
                break
        else:
            return True, i

    return False


t = "Hello world! Nice to meet you"
p = "llo"
result = search(t, p)
print(result)