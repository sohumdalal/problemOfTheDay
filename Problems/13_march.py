'''
Problem Of The Day - 3/13/2025

Move Zeros to the End

Given an array of integers, write a function that moves all zeros in the array to the end without changing the order of non-zero elements.

Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Input: [0, 0, 1]
Output: [1, 0, 0]

Constraints:
Do this in O(n) time complexity.
Do not use extra space for another array. Try to do this in-place.
You may assume that the input array has at least one element.
Hint: Think about how you can swap the zeros with the first non-zero elements and keep a pointer for the position where the next non-zero element should go.

'''