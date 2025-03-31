'''
Solution Of The Day - 3/14/2025

Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
Example:
Input: "abcabcbb"
Output: 3 

Input: "bbbbb"
Output: 1

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
The input string will contain only English letters, digits, symbols, and spaces.
The time complexity should be O(n), where n is the length of the string.
Hint: You can use a sliding window approach.
'''

'''
Solution 1: Two-pointers & Set
Time Complexity: O(N)
In the sliding window, each character is checked at most twice (once when added, once when removed), 
hence O(N) + O(N) = O(N)
Space Complexity: O(min(n, 26)) – why?
'''

def lengthOfLongestSubstring(s):
    charSet = set()
    left = 0 
    maxLength = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        
        charSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength

'''
Solution 2: Brute Force with Set
Time Complexity: O(N2)
In the brute force, each character is checked multiple times in a nested for loop, hence O(N2)
Space Complexity: O(n) (storing substrings)
'''

def bruteForceLongestSubstring(s):
    n = len(s)
    maxLength = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            maxLength = max(maxLength, j - i + 1)

    return maxLength