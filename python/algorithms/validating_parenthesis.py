from collections import deque

def is_valid_bracket(s):
    parenthesis_q = deque()
    flower_bracket_q = deque()
    square_bracket_q = deque()
    ret = True
    for c in s:
        if c == '(':
            parenthesis_q.append(c)
        if c == '{':
            flower_bracket_q.append(c)
        if c == '[':
            square_bracket_q.append(c)
        if c == ')':
            if len(parenthesis_q) == 0:
                ret = False
                break
            parenthesis_q.pop()
        if c == '}':
            if len(flower_bracket_q) == 0:
                ret = False
                break
            flower_bracket_q.pop()
        if c == ']':
            if len(square_bracket_q) == 0:
                ret = False
                break
            square_bracket_q.pop()

    if len(parenthesis_q) != 0 or len(flower_bracket_q) !=0 or len(square_bracket_q) != 0:
        ret = False
    return ret

print(is_valid_bracket("{}()[]"))
print(is_valid_bracket("{}()][]["))
print(is_valid_bracket("()())()"))
print(is_valid_bracket("(()"))

# Remove Invalid Parentheses
"""
Input  : str = “()())()” -
Output : ()()() (())()
There are two possible solutions
"()()()" and "(())()"

Input  : str = (v)())()
Output : (v)()()  (v())()
"""

def remove_invalid_parenthesis(s):
    res = []
    string_q_to_explore = deque()
    visited_strings = set()

    string_q_to_explore.append(s)
    visited_strings.add(s)

    while(len(string_q_to_explore) > 0):
        current_str = string_q_to_explore.pop()
        if is_valid_bracket(current_str):
            # res.append(current_str)
            print(current_str)
            continue # the string at this level has valid formation, so no need to split it further

        for i in range(len(current_str)):
            c = current_str[i]
            if not (c == '(' or c == ')'):
                continue

            new_string = current_str[0:i] + current_str[i+1:] # remove ith character
            if new_string not in visited_strings:
                visited_strings.add(new_string)
                string_q_to_explore.append(new_string)
    return res

remove_invalid_parenthesis("()())()")
remove_invalid_parenthesis("()v)")