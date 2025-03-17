'''
Solution Of The Day - 3/11/2025

Problem: Missing Number in an Array

You are given a list of n numbers ranging from 0 to n, but exactly one number is missing. Write a function to find the missing number in the list.

Examples:
Input: [3, 0, 1]
Output: 2

Input: [0, 1]
Output: 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Constraints:
The input list contains unique numbers.
The numbers range from 0 to n, inclusive.
The list length is n, meaning one number is missing.

Bonus Challenge:
Solve this in O(n) time and O(1) space (not counting input storage).
'''

# Solution 1: Brute Force / Two-Loops
# Time Complexity: O(N^2)
# Space Complexity: O(1)

def missingNum (list):
  n = len(list)
  for i in range(n + 1):
    found = False
    for num in list:
      if num == i:
        found = True
    if not found:
      return i

# Solution 2: Using a Set
# Time Complexity: O(N)
# Space Complexity: O(N)

def missingNum2 (list):
  numSet = set(list)
  n = len(list)
  for i in range(n + 1):
    if i not in numSet:
      return i

# Solution 3: Using a formula for the sum of the first n natural numbers
# Time Complexity: O(N)
# Space Complexity: O(1)

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum