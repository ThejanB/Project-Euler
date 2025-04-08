
def main(L):
    candidates  = list(range(L+1))
    for n in range(2, L+1):
        if candidates[n] == n:
            for k in range(n, L+1, n):
                candidates[k] -= candidates[k] // n
    
    # φ(n) = candidates[n]

    for i in range(3, L+1):
        candidates[i] += candidates[i-1]
    return candidates

pre_computed_list = main(1000000)

for _ in range(int (input())):
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(pre_computed_list[n])
