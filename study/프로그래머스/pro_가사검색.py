def solution(words, queries):
    answer = []
    W = len(words)
    Q = len(queries)
    for i in range(Q):
        cnt = 0
        key = queries[i]
        K = len(key)
        for j in range(W):
            if K == len(words[j]):
                for k in range(K):
                    if key[k] == "?":
                        continue
                    elif key[k] != words[j][k]:
                        break
                else:
                    cnt += 1
        answer.append(cnt)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = solution(words, queries)
print(result)

