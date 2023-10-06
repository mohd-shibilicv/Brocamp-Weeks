def reversed_string(string):
    stack = []

    for char in string:
        stack.append(char)
    
    reversed_str = ""

    while stack:
        reversed_str += stack.pop()

    return reversed_str


string = "Reversed String"

reversed_string = reversed_string(string)

print(reversed_string)
