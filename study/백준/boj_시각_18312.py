'''
5 3
'''

N, K = input().split()
# print(N, K)
st = ['00', '00', '00']
stcom = st[0] + st[1] + st[2]
# stnum = int(stcom)
if len(N) == 1:
    etcom = '0' + N + '5959'
else:
    etcom = N + '5959'
# etnum = int(etcom)

# print(stcom, etcom)


cnt = 0
while stcom <= etcom:
    if K in stcom:
        cnt += 1
    tmp1 = str(int(st[2]) + 1)
    if len(tmp1) == 1:
        st[2] = '0' + tmp1
    else:
        st[2] = tmp1
    if int(st[2]) == 60:
        st[2] = '00'
        tmp2 = str(int(st[1]) + 1)
        if len(tmp2) == 1:
            st[1] = '0' + tmp2
        else:
            st[1] = tmp2
    if int(st[1]) == 60:
        st[1] = '00'
        tmp3 = str(int(st[0]) + 1)
        if len(tmp3) == 1:
            st[0] = '0' + tmp3
        else:
            st[0] = tmp3
    stcom = st[0] + st[1] + st[2]
print(cnt)



