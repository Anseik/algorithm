a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)
c = [0] * (max(a)+1)

print(a)
for i in range(len(a)):
    c[a[i]] += 1

for j in range(1, len(c)):
    c[j] += c[j-1]
print(c)

# a를 뒤에서 부터 순회하며 해당 value(1)를 index로 가지는
# c의 value(4)를 1감소시키고 감소한 값(3)을 index로 가지는 b의 위치에
# a의 value값(1)을 집어넣는다.
for k in range(len(a)-1, -1, -1):
    # print(a[k])
    c[a[k]] -= 1
    b[c[a[k]]] = a[k]


print(b)







