"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive
characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
"""

def encode(s: str):
    ret = ""
    count = 0
    i = 0
    while(i < len(s)):
        c = s[i]
        while(i+1 < len(s) and s[i] == s[i+1]):
            print(s[i])
            count += 1
            i = i+1
        if count > 0:
            ret = ret + c + str(count)
        else:
            ret = ret + c
        count = 0
        i = i +1
    print(ret)
    return ret

def decode(s: str):
    ret = ""
    char = None
    count = -1
    i = 0
    # A3B2C1DA1
    while(i < len(s)):
        char = s[i]
        print(char)
        i = i+1
        c = s[i]
        if c > '0' and  c <'9':
            count = int(c)
            ret = ret + char + char * count
            i = i+1
        else:
            ret = ret + char
    return ret

print("AAAABBBCCDAA" == decode(encode("AAAABBBCCDAA")))
