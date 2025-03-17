'''
Solution Of The Day - 3/12/2025

Check If Number Is A Palindrome

Given an integer, write a function to check if it is a palindrome. A palindrome number is a number that reads the same forward and backward.

Examples:
Input: 121
Output: True

Input: -121
Output: False (negative numbers are not palindromes)

Input: 10
Output: False

Constraints:
The input is a 32-bit signed integer.
You cannot convert the integer to a string (for an extra challenge, avoid string-based solutions!).
'''

# Solution 1: Creating A New Number
# Time Complexity: O(logN)
# Space Complexity: O(1)

def palindromeNum(num):
  if num < 0:
        return False
  reverseNum = 0
  temp = num
  while temp != 0:
    digit = temp % 10
    reverseNum = reverseNum * 10 + digit
    temp = temp//10
  if num == reverseNum:
    return True
  else:
    return False

# Solution 2: Boring One Liner (don’t do this)
# Time Complexity: O(N)
# Space Complexity: O(N)

def palindromeNum(num):
    return str(num) == str(num)[::-1]

# Solution 3: Integer Extraction
# Time Complexity: O(N)
# Space Complexity: O(N)

def palindromeNum(num):
    if num < 0:
        return False

    digits = []
    temp = num

    while temp > 0:
        digits.append(temp % 10)
        temp //= 10  # Integer division

    return digits == digits[::-1]