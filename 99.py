from time import time
start = time()

import math

file = open("99 Project Euler.Txt",'r')
text = file.read()

raws = text.split('\n')         # list of raws
number_list = []

for i in raws:
    number_list.append(i.split(','))

max_number = 0
for i in number_list:
    lg_k = int(i[1])*math.log10(int(i[0]))
    if lg_k > max_number:
        max_number = lg_k
        line = i

print(number_list.index(line)+1)
print(time()-start,'seconds')
