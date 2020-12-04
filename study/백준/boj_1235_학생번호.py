import sys
sys.stdin = open('boj_1235_학생번호.txt')

N = int(input())
students = []
for i in range(N):
    students.append(input())
# print(students)

cnt = 1
idx = -1
while True:
    check = set()
    for i in range(N):
        check.add(students[i][idx:])
    if len(check) == N:
        break
    else:
        idx -= 1
        cnt += 1
print(cnt)

