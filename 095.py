from time import time

#a list of sum of proper divisors
def divisors_sum (limit):
    candidates = [1]*(limit+1)
    for i in range(2,limit//2+1):
        candidates[i*2::i] = [j+i for j in candidates[i*2::i] ]
    return candidates

def calc(limit=1_000_000):
    divisors = divisors_sum (limit)         # divisors sum list
    #print(divisors)
    longest_chain = [0,1]                   # answer = (chain length,mimimum number)
                                            # this is not the actual minimum number 
                                            # chain[k:] means the length after chain [k]

    for i in range(2,limit):              # check every number
        n, chain = i, []
        
        while divisors[n] < limit:
            divisors[n], n = limit+1, divisors[n]

            try: k = chain.index(n)
            except ValueError: chain.append(n)
            else: 
                if len(chain[k:]) > longest_chain[0]:
                    longest_chain = [len(chain[k:]), min(chain[k:])]
            #print(chain)
    return longest_chain[1]

start = time()
mimimum_number = calc()
print("mimimum number :", mimimum_number)
print(time()-start,'seconds')
