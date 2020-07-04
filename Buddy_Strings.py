"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters
in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true

Example 2:
Input: A = "ab", B = "ab"
Output: false

Example 3:
Input: A = "aa", B = "aa"
Output: true

Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:
Input: A = "", B = "aa"
Output: false
"""


class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        mistakes = 0
        first = -1
        second = -1
        letters = dict()
        for i in range(len(A)):
            if A[i] != B[i]:
                mistakes += 1
                if mistakes > 2:
                    return False
                if first == -1:
                    first = i
                else:
                    second = i
            if A[i] in letters:
                letters[A[i]] += 1
            else:
                letters[A[i]] = 1
        return (mistakes == 2 and A[first] == B[second] and B[first] == A[second]) \
               or (mistakes == 0 and max(letters.values()) >= 2)


if __name__ == "__main__":
    print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
    # True
    print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
    # False
    print(Solution().buddyStrings('aaabb', 'aaabb'))
    # True
