import math
import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)


for line in data:
    try:
        N = int(line)
    except:
        continue
    if N < 1:
        continue

    n = 3  # numerator for 1st expansion
    d = 2  # denominator for 1st expansion

    for i in range(2, N + 1):
        n, d = n + 2 * d, n + d

        if int(math.log10(n)) > int(math.log10(d)):
            sys.stdout.write(str(i) + "\n")
