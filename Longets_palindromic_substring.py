"""
A palindrome is a sequence of characters that reads the same backwards and forwards.
Given a string, s, find the longest palindromic substring in s.
"""

class Solution:  # O(n^2)
    def get_palindrom(self, s, left, right):
        while left > 0 and right < len(s) and s[left - 1] == s[right]:
            right += 1
            left -= 1
        return left, right

    def longestPalindrome(self, s):
        lenght = 0
        ans_left = 0
        ans_right = 0
        str_size = len(s)
        for i in range(str_size):
            left, right = self.get_palindrom(s, i, i + 1)
            if right - left > lenght:
                lenght = right - left
                ans_left, ans_right = left, right
            left, right = self.get_palindrom(s, i, i)
            if right - left > lenght:
                lenght = right - left
                ans_left, ans_right = left, right
        return s[ans_left:ans_right]


if __name__ == "__main__":
    s = "mil11lionaaaaaa"
    print(str(Solution().longestPalindrome(s)))
