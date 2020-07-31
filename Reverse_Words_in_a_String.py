"""
Given a string, you need to reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:

    def reverse_str(self, begin, end, str):
        while end > begin:
            str[begin], str[end - 1] = str[end - 1], str[begin]
            end -= 1
            begin += 1

    def reverseWords(self, str1):
        my_str = list(' ' + str1 + ' ')
        begin = 0
        end = 1
        for num in range(len(my_str)):
            if my_str[num] == ' ':
                begin = end
                end = num
                self.reverse_str(begin, end, my_str)
        return "".join(i for i in my_str)


if __name__ == "__main__":
    print(Solution().reverseWords("The cat in the hat"))
    # ehT tac ni eht tah
