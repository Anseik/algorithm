import sys

li = []
for line in sys.stdin:
    # print(line)
    li.append(tuple(map(int, line.split())))

print(li)