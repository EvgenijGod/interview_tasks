class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        a = 0
        list = l1
        while list is not None:
            a = a * 10 + list.val
            list = list.next
        b = 0
        list = l2
        while list is not None:
            b = b * 10 + list.val
            list = list.next
        a += b

        list = ListNode(a % 10)
        tmp = list
        a //= 10
        while a != 0:
            tmp.next = ListNode(a % 10)
            a //= 10
            tmp = tmp.next
        return list
    # Fill this in.

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
