'''
Problem Of The Day - 4/8/2025:

Given a string representing a nested mathematical expression with + and -, return its result. 
Assume valid input.

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''
def evaluate_expression(s):
    stack = []
    num = 0
    sign = 1
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in "+-":
            result += sign * num
            num = 0
            sign = 1 if char == '+' else -1
        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ")":
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()
    return result + sign * num
