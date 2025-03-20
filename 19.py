import time
start = time.time()

year1 = ['31','28','31','30','31','30','31','31','30','31','30','31']
year2 = ['31','29','31','30','31','30','31','31','30','31','30','31']

no_of_days = 0
day = sum(int(day) for day in year2)    # for 1900
year = 1901

while year < 2001:
    if year%4==0:
        for x in year2:
            day += int(x)
            if day%7==6:
                no_of_days += 1
    else:
        for x in year1:
            day += int(x)
            if day%7==6:
                no_of_days += 1
    year += 1
print(no_of_days)

print("\n" , time.time()-start , 'seconds')