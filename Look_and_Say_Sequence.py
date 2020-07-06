"""
A look-and-say sequence is defined as the integer sequence beginning with
a single digit in which the next term is obtained by describing the previous term.
An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.

Your task is, return the nth term of this sequence.
"""


def next_iteration(seq):
    tmp = []
    n = len(seq)
    i = 0
    num = -1
    amnt = 0
    while i < n:
        if amnt == 0:
            num = seq[i]
            amnt += 1
        elif seq[i] == num:
            amnt += 1
        else:
            tmp += [amnt, num]
            amnt = 1
            num = seq[i]
        i += 1
    if amnt != 0:
        tmp += [amnt, num]
    return tmp


if __name__ == "__main__":
    seq = [1]
    iters = 5
    for _ in range(iters):
        seq = next_iteration(seq)
    print(*seq)
