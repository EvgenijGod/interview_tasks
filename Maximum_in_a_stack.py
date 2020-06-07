"""
Implement a class for a stack that supports all the regular functions (push, pop, top)
and an additional function of max() which returns the maximum element
in the stack (return None if the stack is empty).

Each method should run in constant time.
"""


class MaxStack:
    def __init__(self):
        self.__storage = []
        self.__gratest = None
        self.__n = 0

    def push(self, val):
        a = True
        if self.__n == 0:
            self.__gratest = val
        elif val > self.__gratest:
            self.__storage.append(2 * val - self.__gratest)
            self.__gratest = val
            a = False
        self.__n += 1
        if a:
            self.__storage.append(val)

    def pop(self):
        if self.__n == 0:
            return None
        self.__n -= 1
        tmp = self.__storage[self.__n]

        if tmp > self.__gratest:
            self.__gratest = 2 * self.__gratest - tmp

    def top(self):
        if self.__n == 0:
            return None
        tmp = self.__storage[self.__n - 1]
        if tmp > self.__gratest:
            return self.__gratest
        return tmp

    def max(self):
        return self.__gratest


if __name__ == "__main__":
    s = MaxStack()
    s.push(1)
    print(s.top())
    s.push(2)
    print(s.top())

    s.push(3)
    print(s.top())

    s.push(2)
    print(s.top())

    print(s.max())
    # 3
    s.pop()
    s.pop()
    print(s.max())
    # 2
