test2 = 'SSADADAAASADAAAS'
L = len(test2)
N = 5


max_key = ''
max_val = 0
for i in range(0, L - 4):
    tmp = test2[i:i+5]
    my_dict = {}
    for j in range(N):
        if tmp[j] in my_dict:
            my_dict[tmp[j]] += 1
        else:
            my_dict[tmp[j]] = 1

    for key, val in my_dict.items():
        if max_val < val:
            max_val = val
            max_key = key

print(max_key)


my_dict = {}
max_key = ''
max_val = 0
for i in range(L):
    if test2[i] in my_dict:
        my_dict[test2[i]] += 1
    else:
        my_dict[test2[i]] = 1

    if max_val < my_dict[test2[i]]:
        max_val = my_dict[test2[i]]
        max_key = test2[i]

    if i >= N:
        my_dict[test2[i-N]] -= 1

print(max_key, max_val)


