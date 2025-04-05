from itertools import permutations

product_numerator,product_denominator = 1,1
for i in permutations(['1','2','3','4','5','6','7','8','9'],3):
    if int(i[0]+i[1])/int(i[1]+i[2]) == int(i[0])/int(i[2]):
        print(int(str(i[0])+str(i[1])) ,"/",int(str(i[1])+str(i[2])))
        product_numerator *= int(i[0])
        product_denominator *= int(i[2])

print("\n",product_numerator,"/",product_denominator)
print("answer = " , product_denominator/product_numerator)
