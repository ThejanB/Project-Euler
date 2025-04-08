import math

def generate_primes(k):
    candidates = list(range(k+1))
    candidates[4::2] = [None]*(k//2 - 1)
    for i in range(3,int(k**.5 +1),2):
        if candidates[i]:
            candidates[i*2::i] = [None]*(k//i - 1)
    return [i for i in candidates[2:] if i]

def precompute(max_N = 10**7):

    primes = generate_primes(int(math.sqrt(max_N)) + 2)
    
    sums = set()
    
    for p in primes:
        fourth_power = p ** 4
        if fourth_power > max_N:
            break
        for q in primes:
            cube = q ** 3
            if fourth_power + cube > max_N:
                break
            for p in primes:
                square = p ** 2
                total = square + cube + fourth_power
                if total <= max_N:
                    sums.add(total)
                else:
                    break
    
    sorted_sums = sorted(sums)
    count = [0] * (max_N + 1)
    current_count = 0
    index = 0
    length = len(sorted_sums)
    
    for n in range(1, max_N + 1):
        if index < length and sorted_sums[index] == n:
            current_count += 1
            index += 1
        count[n] = current_count
    
    return count

count = precompute() # Or max input
for _ in range(int(input())):
    N = int(input())
    print(count[N])
