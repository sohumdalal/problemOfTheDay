'''
Problem Of The Day - 4/23/2025:

Given a list that may contain nested lists, return a flat list.

Input: [1, [2, [3, 4], 5], 6]
Output: [1, 2, 3, 4, 5, 6]

Can you use recursion?

'''

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    return result

# Test
print(flatten([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]
