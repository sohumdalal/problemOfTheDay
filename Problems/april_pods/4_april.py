'''
Problem Of The Day - 4/4/2025:

You are given a m × n grid. You start at the top-left corner and can only move right or down. How many unique paths exist to reach the bottom-right corner?

Example:
Input: m = 3, n = 2
Output: 3
--- Paths: Right → Right → Down, Right → Down → Right, Down → Right → Right

Hint:
Use recursion with memoization.
paths(m, n) = paths(m-1, n) + paths(m, n-1)

'''