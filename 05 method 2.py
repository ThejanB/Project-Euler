numbers = list(range(1, 21))

# Start with the maximum value among the numbers, as the LCM cannot be less than this
lcm = max(numbers)

# Brute force approach: keep increasing lcm by the maximum number until it is divisible by all numbers
# The time complexity of this algorithm is O(n * lcm) where n is the number of elements in the input list and lcm is the least common multiple of the numbers in the list. 
# The worst-case scenario is when the numbers are all prime numbers. This results in a time complexity of O(n * product of all numbers).
# Not the best approach, but enough
while True:
    for num in numbers:
        if lcm % num != 0:
            break
    else:
        print(lcm)
        break
    lcm += max(numbers)