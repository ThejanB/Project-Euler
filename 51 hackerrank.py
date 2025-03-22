import itertools

def prime_list(n):
    candidates = list(range(n+1))
    candidates[4::2] = [None]*(n//2 -1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:candidates[i*i::i] = [None]*(n//i -(i-1))
    return candidates

def main():
    N, K, L = map(int, input().split())

    lower, upper = 10**(N-1), 10**N - 1
    is_prime = prime_list(upper)
    
    # Generate all N-digit primes
    primes = [p for p in range(lower, upper + 1) if is_prime[p]]
    
    for prime in primes:
        s = str(prime)
        unique_digits = set(s)
        
        for digit in unique_digits:
            # Find all positions of the current digit
            positions = [i for i, ch in enumerate(s) if ch == digit]
            
            # Only proceed if there are at least K positions to replace
            if len(positions) >= K:
                # Sort positions in reverse to prioritize rightmost digits
                sorted_positions = sorted(positions, reverse=True)
                
                # Generate all combinations of K positions to replace
                for selected in itertools.combinations(sorted_positions, K):
                    family = []
                    
                    for replacement_digit in '0123456789':
                        temp = list(s)
                        
                        # Replace the selected positions with the replacement digit
                        for pos in selected:
                            temp[pos] = replacement_digit
                        
                        # Skip numbers with leading zeros
                        if temp[0] == '0':
                            continue
                        new_num = int(''.join(temp))  # Convert back to integer
                        
                        # Check if the new number is prime
                        if new_num >= lower and is_prime[new_num]:
                            family.append(new_num)
                    
                    # Check if the family size meets or exceeds the required size
                    if len(family) >= L:
                        print(*sorted(family)[:L])  # Print the first L primes in the family in sorted order
                        return
main()	