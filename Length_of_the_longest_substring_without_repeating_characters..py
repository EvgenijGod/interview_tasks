"""
Given a string, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        a = set()
        first = 0
        second = 0
        ans = 0
        n = len(s)
        while first < n and second < n:
            if s[second] in a:
                a.remove(s[first])
                first += 1
            else:
                a.add(s[second])
                second += 1
                ans = max(ans, second - first)
        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
    print(Solution().lengthOfLongestSubstring('aaaaccaaabaaccbc'))
