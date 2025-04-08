x,y,tot = 1,2,0

while y<4000000:
    if y%2==0:
        tot += y
    x,y = y,x+y
print(tot)
