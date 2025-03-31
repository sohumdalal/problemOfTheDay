'''
Problem Of The Day - 4/2/2025

Write a function that calculates the Nth Fibonacci number using memoization to optimize repeated calculations.

Example:
fib(10) → 55
fib(20) → 6765

Hint: Use a dictionary to store already computed results.
'''

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# Example usage
print(fib(10))  # Output: 55
print(fib(20))  # Output: 6765
