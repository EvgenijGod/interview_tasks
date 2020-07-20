"""
Given a list of words, group the words that are anagrams of each other.
(An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
"""


def hash_fun(str):
    hash1 = 0
    hash2 = 0
    hash3 = 0
    hash4 = 0
    for i in str:
        num = ord(i)
        hash1 ^= num
        hash2 |= num
        hash3 *= num
        hash4 += num
    return hash1 * hash2 * 79 + hash3 * hash4 * 3


def groupAnagramWords(strs):  # O(N + len(all strs))
    tmp = {}
    for i in strs:
        hash = hash_fun(i)
        if hash in tmp:
            tmp[hash].append(i)
        else:
            tmp[hash] = [i]
    return list(tmp.values())


if __name__ == "__main__":
    print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
    # [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
