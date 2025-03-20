from itertools import combinations_with_replacement

# power = int(input())
power = 5
tot = 0 

numbers = 2 
while 9**power * numbers > 10**(numbers-1):
    for digits in combinations_with_replacement(list(range(10)),numbers):
        no = sum([i**power for i in digits])
        # check digiits and no has same digits
        if sorted(str(no)) == sorted(map(str,digits)):
            tot += no
            print(numbers, no)
    numbers += 1

print('Tot = ' , tot)



