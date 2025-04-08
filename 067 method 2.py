import time
start = time.time()

file = open("067 Project Euler.Txt",'r')
grid = file.read()
file.close()

raws            = grid.split('\n')      #add all numbers to list of raws
number_list     = list()            #list of (list of numbers in raw) - [[],[],[],[],[]]

for x in raws:
        number_raw_list = x.split(' ')
        number_list.append(number_raw_list)     # a list of number list raws

for raw in range(len(number_list),0,-1):     # down to up - 14 th raw -> 1 st raw  (tatal raws = 15 raws)
        for number in range(raw-1):
                number_list[raw-2][number] = int(number_list[raw-2][number]) + max(int(number_list[raw-1][number]),int(number_list[raw-1][number+1]))

print(number_list[0][0])
print(time.time()-start , 'seconds')
