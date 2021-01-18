import sys
num = int(sys.stdin.readline().rstrip())
num_li = list(map(int, sys.stdin.readline().rstrip()))

# print(num)
# print(num_li)

multi = 1
result = 0
for i in range(len(num_li) - 1, -1, -1):
    tmp = num * num_li[i]
    print(tmp)
    result += tmp * multi
    multi *= 10

print(result)
