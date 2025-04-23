'''
Problem Of The Day - 4/23/2025:

Given a list that may contain nested lists, return a flat list.

Input: [1, [2, [3, 4], 5], 6]
Output: [1, 2, 3, 4, 5, 6]

Can you use recursion?

'''

def flatten(array, index = 0, final = []):
    if not isinstance(array, list):
        print("array", array)
        return final
    else:
        if isinstance(array[index], list):
            flatten(array[index], 0, final)
        else:
            print("final:", final)
            final.append(array[index])
            flatten(array[index + 1], index + 1, final)
                 

print(flatten([1, [2, [3, 4], 5], 6]))

