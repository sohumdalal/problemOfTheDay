'''
Problem Of The Day - 4/21/2025:

Implement a function power(x, n) that computes x^n efficiently.
Use recursion and handle negative exponents.

Input: power(2, 10)
Output: 1024
(Hint: Use x^n = (x^2)^(n/2) when n is even)

'''

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x, n - 1)

# Test
print(power(2, 10))  # Output: 1024
print(power(2, -2))  # Output: 0.25