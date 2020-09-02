"""
Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment
can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1].
The function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        ans = 0
        while x:
            if x > 0:
                num = x % 10
                x //= 10
                if 2 ** 31 / 10 < ans:
                    return 0
                ans = ans * 10 + num
            else:
                num = -x % 10 + 10
                x //= 10
                if (2 ** 31 - 1) / 10 < -ans:
                    return 0
                ans = ans * 10 - num
        return ans


if __name__ == "__main__":
    print(Solution().reverse(123))
    # 321
    print(Solution().reverse(2 ** 31))
    # 0
