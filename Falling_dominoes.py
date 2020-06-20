"""
Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends,
the force cancels out and that domino remains upright.
"""


def cmp(a, b):
    return (a > b) - (a < b)


class Solution(object):
    def pushDominoes(self, dominoes):
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y:  # RL
                for k in range(i + 1, j):
                    ans[k] = '.LR'[cmp(k - i, j - k)]

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().pushDominoes('..R...L..R.'))
    # ..RR.LL..RR
