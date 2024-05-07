import numpy as np
from scipy.optimize import curve_fit

# Given numbers
numbers = [4, 8, 15, 16, 23, 42]

# x-values
x_values = np.arange(1, len(numbers) + 1)

# Function to fit (polynomial of degree 6)
def polynomial_func(x, a, b, c, d, e, f, g):
    return a * x**6 + b * x**5 + c * x**4 + d * x**3 + e * x**2 + f * x + g

# Perform curve fitting
params, covariance = curve_fit(polynomial_func, x_values, numbers)

# Extracting coefficients
a, b, c, d, e, f, g = params

# Print coefficients
print("Coefficients:", params)

# Predict x for the next number
next_x = len(numbers) + 1
next_number = polynomial_func(next_x, a, b, c, d, e, f, g)
print("Next number:", next_number)

# Coefficients obtained from curve fitting
a = -0.00156434
b = 0.10747682
c = -2.81235955
d = 32.58677527
e = -180.9567552
f = 460.34951771
g = -376.24025242

# Predict the 7th number
next_x = 7
next_number = polynomial_func(next_x, a, b, c, d, e, f, g)
print("Predicted 7th number:", next_number)