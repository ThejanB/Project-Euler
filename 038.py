from time import time
start = time()

target = ['1','2','3','4','5','6','7','8','9']
max_pandigital = 0
for no in range(9,9999):
    no_srting = ""
    i = 1
    no_list = []
    while len(no_srting) < 9:   # create a number containing more than 8 digits
        no_srting += str(no*i)
        i += 1
    if len(no_srting) != 9 or '0' in no_srting:
        continue
    for j in no_srting:         #create no_list
        no_list.append(j)
    no_list.sort()
    if no_list ==  target and max_pandigital < int(no_srting):
        max_pandigital = int(no_srting)
print(max_pandigital)

print('\n',time()-start , 'seconds')
