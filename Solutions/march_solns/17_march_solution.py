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

# Solution 1: Sliding Window
# Time Complexity: O(n), since each character is processed once (add/remove operations).
# Space Complexity: O(1), since we only use two fixed-size arrays of 26 elements.


def findAnagrams(s, p):
    from collections import Counter  
    
    m, n = len(p), len(s)
    if m > n:
        return []
    
    p_count = Counter(p)  
    s_count = Counter(s[:m])  
    result = []
    
    if p_count == s_count:
        result.append(0)

    for i in range(m, n):
        start_idx = i - m  

        s_count[s[start_idx]] -= 1
        if s_count[s[start_idx]] == 0:
            del s_count[s[start_idx]]  
        
        s_count[s[i]] = s_count.get(s[i], 0) + 1

        if s_count == p_count:
            result.append(start_idx + 1)

    return result

print(findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]
