import math
import sys

input = sys.stdin.read
data = input().split()
T = int(data[0])
nums = list(map(int, data[1:]))

for x in nums:
    # Discriminant: 1 + 8x
    d = 1 + 8 * x
    root = int(math.sqrt(d))
    if root * root != d:
        print(-1)
        continue
    n = (-1 + root)
    if n % 2 != 0:
        print(-1)
    else:
        print(n // 2)

# You can solve the triangle number formula in reverse, as a quadratic equation.
# The formula for the nth triangle number is n*(n+1)/2 = t
# Rearranging this equation gives n^2 + n - 2t = 0
# The discriminant of this quadratic equation is 1 + 8t
