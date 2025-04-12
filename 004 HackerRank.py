t = int(input().strip())
for a0 in range(t):
    limit = int(input().strip())
    
    maxproduct,maxy,maxx = 0,0,0

    for x in range(990,100,-11):            # x divides by 11
            for y in range(999,100,-1):
                    product = x*y
                    if product < maxproduct and product< limit:
                            break
                    if product == int(str(product)[::-1]) and product< limit :
                            maxproduct,maxx,maxy = product,x,y
                            break
    # print("x =" , maxx)
    # print("y =" , maxy)
    print(maxproduct)
