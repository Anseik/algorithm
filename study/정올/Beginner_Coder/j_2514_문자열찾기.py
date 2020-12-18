import sys
target = sys.stdin.readline().rstrip()

koi_cnt = 0
ioi_cnt = 0
for i in range(len(target) - 2):
    if target[i:i + 3] == 'KOI':
        koi_cnt += 1
    elif target[i:i + 3] == 'IOI':
        ioi_cnt += 1

print(koi_cnt)
print(ioi_cnt)