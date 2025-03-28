
N, K = map(int, input().split())

if K == 8:
    target = ['1','2','3','4','5','6','7','8']
else:
    target = ['1','2','3','4','5','6','7','8','9']

for no in range(9,N):
    no_srting = ""
    i = 1
    while len(no_srting) < K:   # create a number containing more than 8 digits
        no_srting += str(no*i)
        i += 1
    if len(no_srting) != K or '0' in no_srting:
        continue
    no_list = list(no_srting)
    no_list.sort()
    if no_list ==  target:
        print(no)

