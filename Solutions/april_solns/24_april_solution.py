'''
Problem Of The Day - 4/24/2025:

Write a function that checks if two words differ by exactly one letter.

Input: "cold", "cord" → True
Input: "cold", "warm" → False

Bonus: Apply this to filter a list of neighbors.

'''

def one_letter_diff(word1, word2):
    if len(word1) != len(word2):
        return False
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

# Test
print(one_letter_diff("cold", "cord"))  # Output: True
print(one_letter_diff("cold", "warm"))  # Output: False