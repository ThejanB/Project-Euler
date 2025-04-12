from time import time
start = time()

e = [2]
i = 0
while len(e) < 100:
    i += 1
    e.extend([1,2*i,1])

numerator = 1
denominator = e.pop()
for i in e[::-1]:
    denominator,numerator = denominator*i+numerator,denominator
else:
    numerator,denominator = denominator,numerator

print(sum(int(i) for i in str(numerator)))
print(time()-start,"seconds")



'''
Question gives the pattern of list e,
    e = [2,   ... 1,2k,1 ... ]
-so we can get list e easily by using a while loop

numerator/denominator = 1 /(i + previous_numerator/previous_denominator)
                      = previous_denominator/(previous_denominator*i + previous_numerator)

    so,
    numerator   = previous_denominator
    denominator = previous_denominator*i + previous_numerator
-so we can use a for loop for this calculate


in final case, i = e[-1] = 2
    e = 2 + previous_numerator/previous_denominator
      = (previous_denominator*2 + previous_numerator) /previous_denominator
      =  denominator/numerator
     so we have to change values at the end of for loop

then we can calculate the sum of digits in the numerator

Thejan -> 2021-03-11

'''
