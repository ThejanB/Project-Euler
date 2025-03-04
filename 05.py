ans = 1
limit = 20

for i in range(1, limit+1):
    if ans % i > 0:
        for j in range(1, limit+1):
            if (ans*j) % i == 0:
                ans *= j
                break
print(ans)