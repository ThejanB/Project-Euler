cache = {"max": [1, 1]}  # Store last tested triangle number and index
last_cache_value = 0
def count_factors(n):
    if n in cache:
        return cache[n]

    count = 0
    sqrt_n = int(n ** 0.5)
    for x in range(1, sqrt_n + 1):
        if n % x == 0:
            count += 2  # Count both `x` and `n/x`

    if sqrt_n * sqrt_n == n:  # If n is a perfect square, adjust count
        count -= 1
    
    return count

def first_triangle_with_divisors(n):
    
    """ Finds the first triangular number with over n divisors """
    
    global last_cache_value
    
    if n in cache:
        return cache[n]
    
    x, T_no = cache["max"]  # Start from last checked triangle number
    count = count_factors(T_no)
    
    while count <= n:
        x += 1
        T_no += x
        count = count_factors(T_no)
        if count-1 not in cache:
            for k in range(last_cache_value+1,count):
                cache[k] = T_no
            last_cache_value = count-1
        
    if n not in cache:
        cache[n] = T_no
            
    cache["max"] = [x, T_no]  # Update last checked values
    
    return T_no

t = int(input())
for _ in range(t):
    n = int(input())
    print(first_triangle_with_divisors(n))
