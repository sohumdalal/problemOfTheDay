'''
Problem Of The Day - 4/22/2025:

Write a recursive function that counts the number of vowels in a given string.
No loops allowed!

Input: "recursion is cool"
Output: 6

'''

def count_vowels(s):
    if not s:
        return 0
    return (1 if s[0].lower() in "aeiou" else 0) + count_vowels(s[1:])

# Test
print(count_vowels("recursion is cool"))  # Output: 6