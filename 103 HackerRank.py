A = [11, 18, 19, 20, 22, 25]
mid = A[int( (len(A)+1)/2 )]

next_A = [mid] + [i+mid for i in A]

ans = ''
for i in next_A:
    ans += str(i)

print(next_A)
print(ans)
    
