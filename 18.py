import time
start = time.time()

numbers = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23  '''

raws = numbers.split('\n')      #add all numbers to list of raws
number_list = list()            #list of (list of numbers in raw) - [[],[],[],[],[]]

for x in raws:
        number_raw_list = x.split(' ')
        number_list.append(number_raw_list)     # a list of number list raws

for raw in range(len(number_list),0,-1):     # down to up - 14 th raw -> 1 st raw  (tatal raws = 15 raws)
        for number in range(raw-1):
                number_list[raw-2][number] = int(number_list[raw-2][number]) + max(int(number_list[raw-1][number]),int(number_list[raw-1][number+1]))

print(number_list[0][0])

print( time.time()-start , 'seconds')
