def counting_sort(a):
    b = [0] * len(a)
    c = [0] * (max(a)+1)

    # count배열을 만든다.
    # for i in range(len(a)):
    #     c[a[i]] += 1

    for i in a:
        c[i] += 1
    # print(c)

    # count배열을 누적으로 만든다.
    for j in range(1, len(c)):
        c[j] += c[j-1]
    # print(c)

    #a를 순회하며 해당하는 count배열의 값을 1씩 감소 시키고 b의 해당 위치에 a의 값을 넣는다.
    # for k in range(len(a)-1, -1, -1):
    #     c[a[k]] -= 1
    #     b[c[a[k]]] = a[k]
    # print(b)

    for k in a:
        c[k] -= 1
        b[c[k]] = k
    return b


a = [0, 4, 1, 3, 1, 2, 4, 1, 5, 6]
result = counting_sort(a)
print(result)