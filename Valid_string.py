"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s):
        stack = []
        len = 0
        for i in s:
            if i is '{' or i is '[' or i is '(':
                stack.append(i)
                len += 1
            elif i is '}':
                if len == 0 or stack.pop() != '{':
                    return False
                len -= 1
            elif i is ')':
                if len == 0 or stack.pop() != '(':
                    return False
                len -= 1
            elif i is ']':
                if len == 0 or stack.pop() != '[':
                    return False
                len -= 1
        if len == 0:
            return True
        return False


if __name__ == "__main__":
    # Test Program
    s = "()(){(())"
    # should return False
    print(Solution().isValid(s))

    s = ""
    # should return True
    print(Solution().isValid(s))

    s = "([{}])()"
    # should return True
    print(Solution().isValid(s))
