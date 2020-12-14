def kth(a, k):
    a.sort()
    ret = a[k - 1]
    return ret