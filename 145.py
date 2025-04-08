count = 0

# 1 didit numbers - no solutions
# 2 didit numbers - ab + ba
for a in [1,3,5,7]:
    for b in [2,4,6,8]:
        if a+b > 10:break
        count += 2                  # ab,ba
            
# 3 didit numbers - abc + cba  , b =[0,1,2,3,4]
for a in [1,3,5,7,9]:
    for c in [2,4,6,8]:
        if a+c < 10:continue
        count += 2*5                # ac,ca  and  b

# 4 didit numbers - abcd +dcba
for a in [1,3,5,7,9]:
    for d in [2,4,6,8]:
        if a+d>10:break
        for b in [1,3,5,7,9]:
            for c in [0,2,4,6,8]:
                if b+c>10:break
                count += 2*2        # ad,da  and  bc,cb

# 5 didit numbers - no solutions
# 6 didit numbers - abcdef+ fedcba
for a in [1,3,5,7,9]:
    for f in [2,4,6,8]:
        if a+f>10:break
        for b in [1,3,5,7,9]:
            for e in [0,2,4,6,8]:
                if b+e>10:break
                for c in [1,3,5,7,9]:
                    for d in [0,2,4,6,8]:
                        if c+d>10:break
                        count += 2*2*2      # af,fa  and  be,eb and  cd,dc

# 7 didit numbers - abcdefg + gfedcba ,d =[0,1,2,3,4]
for a in [1,3,5,7,9]:
    for g in [2,4,6,8]:
        if a+g<10:continue
        for b in [i for i in range(10)]:
            for f in [j for j in range(10)]:
                if b+f>9:break
                if (b+f)%2 == 1:continue
                for c in [1,3,5,7,9]:
                    for e in [0,2,4,6,8]:
                        if c+e<10:continue
                        count += 2*2*5  #ag,ga and bf,fb and d

# 8 didit numbers - abcdefgh + hgfedcba
for a in [1,3,5,7,9]:
    for h in [2,4,6,8]:
        if a+h>10:break
        for b in [1,3,5,7,9]:
            for g in [0,2,4,6,8]:
                if b+g>10:break
                for c in [1,3,5,7,9]:
                    for f in [0,2,4,6,8]:
                        if c+f>10:break
                        for d in [1,3,5,7,9]:
                            for e in [0,2,4,6,8]:
                                if d+e>10:break
                                count += 2*2*2*2
# 9 didit numbers - no solutions
    
print(count)
    
'''
->1 digit numbers
    It is easy to see that every 1 digit number is not reversible.
        n+reverse(n) = n+n = 2*n , it is a even number

->9 digit numbers
    -We have four pairs and a middle digit. I will number the four pairs 1,2,3,4 since using inner and outer might get a bit confusing.
         1,2,3,4,middle_digit,4,3,2,1
         
         i1 i2 i3 i4 i5 i6 i7 i8 i9
       + i9 i8 i7 i6 i5 i4 i3 i2 i1
         
    -The middle digit must as always get a carry over, so pair 4 must have a carry over.
    -If pair 4 has a carry over it will deliver a carry over to pair 3 and thus, pair 2 must also deliver a carry over to pair 3.
    -If pair 2 have a carry over then left pair 1 will receive a carry over while right pair 1 not ,
    -which means that it will end up with different parities.
        if right pair 1 is even ,left pair 1 must be a odd
        if right pair 1 is odd ,left pair 1 must be a even
    -So there are no solutions in this case.

same situation in 5 digit numbers also.so no solutions for 5 digit numbers.

->2 digit numbers
    pair 1,2
        i1 i2
      + i2 i1

    i1+i2 < 10  (not to carry over)
    1 digit must be a even and other digit must be a odd ()
    i1 or i2 must not equal to 0

Thejan -> 2021-03-03
'''
