import sys
for line in sys.stdin:
    line = line.rstrip()
    if line == '0':
        break
    else:
        li = []
        sum_result = 0
        for i in range(len(line)):
            li.append(line[i])
            sum_result += int(line[i])
        li.reverse()
        print(int(''.join(li)), sum_result)

