'''
Problem Of The Day - 3/28/2025

Given a string s containing words separated by spaces, 
return the string with the words reversed but keep the order
of characters in each word unchanged.


Input: "hello world this is python"  
Output: "python is this world hello"  

Input: "one two three"  
Output: "three two one"  


Constraints:

--- s contains only lowercase letters and spaces.
--- Words are separated by a single space, and there are no leading or trailing spaces.

Hint:
--- Use .split() and think about how to reverse a list efficiently.
'''

def reverse_words(s):
    words = []
    word = ""
    
    # Manually split words
    for char in s:
        if char != " ":
            word += char
        else:
            if word:  # Avoid multiple spaces
                words.append(word)
                word = ""
    
    if word:  # Add last word if not empty
        words.append(word)

    # Reverse words manually
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    
    # Manually join words with spaces
    result = ""
    for i in range(len(words)):
        result += words[i]
        if i < len(words) - 1:
            result += " "
    
    return result

# Test cases
print(reverse_words("hello world this is python"))  # "python is this world hello"
print(reverse_words("one two three"))              # "three two one"
print(reverse_words("a b c"))                      # "c b a"
print(reverse_words("  leading and trailing  "))   # "trailing and leading"
