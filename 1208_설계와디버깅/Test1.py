test1 = 'ASADADAS'
my_dict = {}

for i in range(len(test1)):
    if test1[i] in my_dict:
        my_dict[test1[i]] += 1
    else:
        my_dict[test1[i]] = 1

# print(my_dict)
max_key = ''
max_val = 0
for key, val in my_dict.items():
    if max_val < val:
        max_val = val
        max_key = key

print(max_key)

