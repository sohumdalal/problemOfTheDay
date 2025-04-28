'''
Problem Of The Day - 4/29/2025:

Write a function that finds the first uppercase letter in a string using recursion.

Input: "helloWorld"
Output: "W"

'''

def find_first_upper(s, idx=0):
    if idx == len(s):
        return None
    if s[idx].isupper():
        return s[idx]
    return find_first_upper(s, idx + 1)

# Example
print(find_first_upper("helloWorld"))  # Output: 'W'
print(find_first_upper("nowords"))     # Output: None