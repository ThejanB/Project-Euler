import numpy as np

# Define the given polynomial generating function
def u(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

# Function to generate the coefficients of the interpolating polynomial
def interpolating_polynomial(x, y):
    return np.polyfit(x, y, len(x)-1)

# Function to evaluate a polynomial at a given point
def evaluate_polynomial(coefficients, x):
    return sum(c * x**i for i, c in enumerate(reversed(coefficients)))

# Compute the sum of FITs
sum_of_fits = 0

# Iterate over k (number of terms used to fit the polynomial)
for k in range(1, 11):
    # Generate the first k terms of the sequence
    x_values = list(range(1, k+1))
    y_values = [u(n) for n in x_values]

    # Find the interpolating polynomial
    coefficients = interpolating_polynomial(x_values, y_values)

    # Calculate the first incorrect term (FIT)
    fit = evaluate_polynomial(coefficients, k+1)

    # Add FIT to the sum
    sum_of_fits += round(fit)

print("Sum of FITs:", sum_of_fits)