'''
Problem Of The Day - 4/30/2025:

Given two sorted Python lists, recursively merge them into one sorted list (no loops allowed).

Input: [1, 3, 5] and [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

'''

def merge_sorted_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]] + merge_sorted_lists(l1[1:], l2)
    else:
        return [l2[0]] + merge_sorted_lists(l1, l2[1:])

# Example
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]