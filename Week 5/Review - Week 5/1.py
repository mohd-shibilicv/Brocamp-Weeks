def valid_brackets(string):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            return False
    
    return not stack

string = "{}[)]"

print(valid_brackets(string))
