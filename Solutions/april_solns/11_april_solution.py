'''
Problem Of The Day - 4/11/2025:

Given a run-length encoded string like "a2b3c1", decode it into "aabbbc".

'''
def decode_rle(s):
    result = ""
    i = 0
    while i < len(s):
        char = s[i]
        count = ""
        i += 1
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        result += char * int(count)
    return result
