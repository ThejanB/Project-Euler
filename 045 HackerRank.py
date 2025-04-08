def triangular(n):
    return n * (n + 1) // 2

def pentagonal(n):
    return n * (3 * n - 1) // 2

def hexagonal(n):
    return n * (2 * n - 1)

def generate_sequence(func, N):
    n = 1
    while (val := func(n)) < N:
        yield val
        n += 1

def find_common_numbers(N, a, b):
    gen_a = generate_sequence(triangular, N) if a == 3 else \
            generate_sequence(pentagonal, N) if a == 5 else \
            generate_sequence(hexagonal, N)
    
    gen_b = generate_sequence(triangular, N) if b == 3 else \
            generate_sequence(pentagonal, N) if b == 5 else \
            generate_sequence(hexagonal, N)
    
    val_a, val_b = next(gen_a, None), next(gen_b, None)
    while val_a is not None and val_b is not None:
        if val_a == val_b:
            print(val_a)
            val_a, val_b = next(gen_a, None), next(gen_b, None)
        elif val_a < val_b:
            val_a = next(gen_a, None)
        else:
            val_b = next(gen_b, None)

if __name__ == "__main__":
    N, a, b = map(int, input().split())
    find_common_numbers(N, a, b)
