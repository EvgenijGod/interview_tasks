"""
You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

Example:

"()())()"

The following input should return 1.

")("

"""


def count_invalid_parenthesis(string):
    n = 0
    stack = []
    for i in string:
        if n == 0:
            n += 1
            stack.append(i)
        else:
            tmp = stack[n - 1]
            if tmp == '(' and i == ')':
                n -= 1
                stack.pop()
            else:
                n += 1
                stack.append(i)
    return n


if __name__ == "__main__":
    print(count_invalid_parenthesis("()())()"))
    # 1
    print(count_invalid_parenthesis("()(((((())()"))
    # 4
