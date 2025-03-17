'''
Solution Of The Day - 3/17/2025

Find All Anagrams in a String

Given a string s and a string p, find all the start indices of p's anagrams in s.
The order of output does not matter.

Example:
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Constraints:
Both strings have lowercase English letters.
The time complexity should be O(n), where n is the length of s.

Hint:
Think about using a sliding window of size equal to the length of p to check each substring in s. You can use a hash map or an array to track the frequency of characters in p and the current window in s.
'''

