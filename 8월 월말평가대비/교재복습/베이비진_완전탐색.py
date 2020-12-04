
def check_babyjin(p):
    for i1 in range(len(p)):
        for i2 in range(len(p)):
            if i2 != i1:
                for i3 in range(len(p)):
                    if i3 != i1 and i3 != i2:
                        for i4 in range(len(p)):
                            if i4 != i1 and i4 != i2 and i4 != i3:
                                for i5 in range(len(p)):
                                    if i5 != i1 and i5 != i2 and i5 != i3 and i5 != i4:
                                        for i6 in range(len(p)):
                                            if i6 != i1 and i6 != i2 and i6 != i3 and i6 != i4 and i6 != i5:
                                                chk = 0
                                                if p[i1] == p[i2] == p[i3]: chk += 1
                                                if p[i4] == p[i5] == p[i6]: chk += 1
                                                if p[i1] + 1 == p[i2] and p[i2] + 1 == p[i3]: chk += 1
                                                if p[i4] + 1 == p[i5] and p[i5] + 1 == p[i6]: chk += 1
                                                if chk == 2:
                                                    return True

    return False

p = [2, 3, 4, 4, 6, 5]
if check_babyjin(p): print('BabyJin입니다.')
else: print('BabyJin이 아닙니다.')

