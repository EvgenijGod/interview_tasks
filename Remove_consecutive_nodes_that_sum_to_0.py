"""
Given a linked list of integers, remove all consecutive nodes that sum up to 0.

Example:
Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
Output: 10

The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed. 4 -> -4
also sums up to 0 too so that sequence should also be removed.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeConsecutiveSumTo0(node):
    begin = node
    sums = dict()
    sum = 0
    while node:
        sum += node.value
        if sum in sums:
            tmp = sums[sum]
            new_sum = sum
            tmp1 = tmp.next
            tmp1.next = node.next
            while tmp1 != node:
                new_sum += tmp1.value
                del sums[new_sum]
                tmp1 = tmp1.next
        elif sum == 0:
            new_sum = 0
            while begin != node:
                new_sum += begin.value
                del sums[new_sum]
                begin = begin.next
            begin = begin.next
        else:
            sums[sum] = node
    return begin


if __name__ == "__main__":
    node = Node(10)
    node.next = Node(5)
    node.next.next = Node(-3)
    node.next.next.next = Node(-3)
    node.next.next.next.next = Node(1)
    node.next.next.next.next.next = Node(4)
    node.next.next.next.next.next.next = Node(-4)
    node = removeConsecutiveSumTo0(node)
    while node:
        print(node.value)
        node = node.next
    # 10
