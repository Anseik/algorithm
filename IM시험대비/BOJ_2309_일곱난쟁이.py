'''
20
7
23
19
10
15
25
8
13
'''

def comb(idx, cnt, tall_sum, selected):
    if tall_sum > 100:
        return
    if cnt == 7:
        if tall_sum == 100:
            case_tall = []
            for i in range(9):
                if selected[i] == 1:
                    case_tall.append(talls[i])
            result.append(case_tall)
            return
        return

    if idx == 9:
        return

    selected[idx] = 1
    comb(idx + 1, cnt + 1, tall_sum + talls[idx], selected)
    selected[idx] = 0
    comb(idx + 1, cnt, tall_sum, selected)

talls = []
for i in range(9):
    talls.append(int(input()))
# print(talls)
selected = [0] * 9
result = []
comb(0, 0, 0, selected)
for k in range(len(result)):
    answer = sorted(result[k])
    for p in answer:
        print(p)
    break
