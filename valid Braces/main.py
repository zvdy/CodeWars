def valid_braces(string):
    braces = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in string:
        if char in braces:
            stack.append(char)
        elif not stack or braces[stack.pop()] != char:
            return False
    return not stack
