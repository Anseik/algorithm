def fibo(n):
    if n < 2:   # 기본파트
        return n
    else:       # 유도파트
        return fibo(n-1) + fibo(n-2)

print(fibo(7))
