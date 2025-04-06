'''
Problem Of The Day - 4/9/2025:

Implement a recursive function to reverse a string.

'''

#Cheat
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

#Better
def reverse_string(s):
    def helper(s, index):
        if index < 0:
            return ""
        return s[index] + helper(s, index - 1)
    
    return helper(s, len(s) - 1)

# Example
print(reverse_string("hello"))  # Output: "olleh"
