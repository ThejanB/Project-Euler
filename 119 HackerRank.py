def convert_to_base(n, base):
    """Converts a number n to a given base and returns the digits as a list."""
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits[::-1]  # Reverse to get the correct order


def find_interesting_numbers(base):
    """Finds all interesting numbers below 10^100 for the given base."""
    interesting_numbers = set()
    limit = 10**100  # Upper limit as per problem statement
    
    for x in range(2, int(1e3)):  # Checking reasonable base values
        power = 1  # Start from exponent 1
        while True:
            num = x ** power
            if num >= limit:
                break
            if sum(convert_to_base(num, base)) == x:
                interesting_numbers.add(num)
            power += 1

    # Sort results in ascending order
    interesting_numbers = sorted(interesting_numbers)
    interesting_numbers = [i for i in interesting_numbers if i > 9]
    
    # Print the result in the required format
    if interesting_numbers:
        print(" ".join(map(str, interesting_numbers)))
    else:
        print("No interesting numbers found.")

# Read input base B
B = int(input().strip())
find_interesting_numbers(B)
