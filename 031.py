from time import time
start = time()

def ways(amount,coins):
    if not coins:
        return 0
    count = 0
    coin_1 = coins[0]
    coins = coins[1::]
    if amount%coin_1 == 0:
        count += 1
    for amount_2 in range(0,amount,coin_1):
        count += ways(amount - amount_2,coins)
    return count

def descending(amount,coins):
    coins.sort(reverse=True)
    return ways(amount,coins)
  
print(descending(200,[1,10,5,2,20,50,100,200]))
print(time()-start,"seconds")


'''
if we didn't convert coins list to descending order, it takes much more time,
becouse the loop in def_ways() can be very long

Thejan -> 28-02-2020
'''
