'''
Problem Of The Day - 4/28/2025:

Write a recursive function that takes a non-negative integer and returns the sum of its digits.

Input: 1234
Output: 10
(1 + 2 + 3 + 4 = 10)

'''

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

# Example
print(sum_digits(1234))  # Output: 10