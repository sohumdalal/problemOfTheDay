'''
Problem Of The Day - 4/25/2025:

Write a function that rotates a 2x2 matrix clockwise.

Input:
[
 [1, 2],
 [3, 4]
]

Output:
[
 [3, 1],
 [4, 2]
]


Bonus: Make it work for any square NxN matrix.

Let me know if you want a version where the rotation is done in-place or without using .reverse() and .zip() tricks.

'''

def rotate_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        return "Not a 2x2 matrix"
    
    a, b = matrix[0]
    c, d = matrix[1]
    
    return [[c, a],
            [d, b]]

# Test
original = [[1, 2], [3, 4]]
rotated = rotate_2x2(original)
print(rotated)  # Output: [[3, 1], [4, 2]]