"""
You are given a string s, and an integer k.
Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff.
The answer should be 5.
"""


def longest_substring_with_k_distinct_characters(s, k):
    begin = 0
    end = 0
    n = len(s)
    storage = dict()
    answer = 0
    while end != n:
        if s[end] not in storage:
            while len(storage) == k:
                storage[s[begin]] -= 1
                if storage[s[begin]] == 0:
                    storage.pop(s[begin])
                begin += 1
            storage[s[end]] = 1
        else:
            storage[s[end]] += 1
        answer = max(answer, end - begin + 1)
        end += 1
    return answer


if __name__ == "__main__":
    print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
    # 5 (because 'defff' has length 5 with 3 characters)
    print(longest_substring_with_k_distinct_characters('aaaaaabcdefff', 2))
    # 5 (because 'aaaaaab' has length 7 with 2 characters)

