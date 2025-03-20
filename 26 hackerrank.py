def cycle_length(d):
    """
    Returns the length of the repeating decimal cycle of 1/d.
    Assumes gcd(d,10) = 1 (i.e., d not divisible by 2 or 5).
    """
    length = 1
    remainder = 10 % d
    while remainder != 1:
        remainder = (remainder * 10) % d
        length += 1
    return length

def main():
    import sys
    
    input_data = sys.stdin.read().strip().split()
    T = int(input_data[0])
    queries = list(map(int, input_data[1:]))

    maxN = max(queries)

    best = [0] * (maxN + 1)
    longest_cycle = 0
    best_d = 0
    
    for d in range(3, maxN + 1):
        if d % 2 != 0 and d % 5 != 0:
            cl = cycle_length(d)
            if cl > longest_cycle:
                longest_cycle = cl
                best_d = d
        best[d] = best_d
    
    output = []
    for n in queries:
        if n > 2:
            output.append(str(best[n - 1]))
        else:
            output.append('0')
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
