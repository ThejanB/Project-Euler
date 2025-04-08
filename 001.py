#method 1
tot = 0
for x in range(0,1000):
    if x%3==0 or x%5==0:
        tot += x
print(tot)

#method 2
print(sum([x for x in range(0,1000) if x%3==0 or x%5==0]))

#method 3 - fasterst method
n = 1000
x = (n-1)//3
tot = 3*((x*(x+1))//2)
x = (n-1)//5
tot += 5*((x*(x+1))//2)
x = (n-1)//15
tot -= 15*((x*(x+1))//2)
        
print(tot)