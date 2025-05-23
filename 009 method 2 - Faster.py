x = 1000

def find_pythagorean_triplet(x):
    max_product = -1
    for a in range(1, x // 3):
        b = (x * (x - 2 * a)) // (2 * (x - a))  # Direct calculation of b
        c = x - a - b
        if c < b:
            break
        if a * a + b * b == c * c:
            a, b, c = sorted([a, b, c])
            print(f"Pythagorean triplet: a={a}, b={b}, c={c}")
            print(f"Product abc: {a * b * c}\n")
            max_product = max(max_product, a * b * c)

    return max_product

# Find the triplet for which a + b + c = x
triplet = find_pythagorean_triplet(x)
print(f"Max product of the Pythagorean triplet for which a + b + c = {x}: {triplet}")
