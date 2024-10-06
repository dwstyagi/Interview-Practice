def isValid(s) -> bool:
    """
    return balanced parenthesis
    """
    stack = []

    if s.length == 0:
        return 1

    i = 0
    while s:
        if s[i] == "[" or s[i] == "(" or s[i] == "{":
            stack.append(s[i])
            continue

        if s[i] == ")":
            if stack[-1] == "[" or stack[-1] == "{":
                return -1
            stack.pop()

        if s[i] == "]":
            if stack[-1] == "(" or stack[-1] == "{":
                return -1
            stack.pop()

        if s[i] == "}":
            if stack[-1] == "[" or stack[-1] == "(":
                return -1
            stack.pop()
        i += 1

        if stack.length == 0:
            return 1
        else:
            return -1
