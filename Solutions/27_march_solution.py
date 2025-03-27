'''
Problem Of The Day - 3/27/2025

Given a string s, determine if you can make it a palindrome by removing exactly one character.

Input: "radkar"  
Output: True  # Remove 'k' → "radar" (Palindrome)

Input: "abcdef"  
Output: False  # No single removal can make it a palindrome

Constraints:
--- s consists of only lowercase letters.
--- 1 ≤ len(s) ≤ 10⁵

Hint:
--- Try checking if s is already a palindrome.
--- If not, see if removing one character from the left or right makes it one.

'''

def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def can_be_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Try skipping either the left or right character
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    
    return True  # Already a palindrome

# Test cases
print(can_be_palindrome("radkar"))  # True (Remove 'k')
print(can_be_palindrome("abcdef"))  # False (No single removal works)
print(can_be_palindrome("racecar")) # True (Already a palindrome)
