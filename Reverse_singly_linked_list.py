"""
Given a singly-linked list, reverse the list.
This can be done iteratively or recursively. Both solutions
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

# Iterative Solution
    def reverseIteratively(self, head):
        next_el = head.next
        prev = None
        head.next = prev
        while next_el is not None:
            prev = head
            head = next_el
            next_el = head.next
            head.next = prev
    # Implement this.

# Recursive Solution
    def reverseRecursively(self, head):
        next_el = head.next
        if next_el is not None:
            self.reverseRecursively(next_el)
            next_el.next = head
            head.next = None
    # Implement this.


if __name__ == "__main__":
    # Test Program
    # Initialize the test list:
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail

    print("Initial list: ")
    testHead.printList()
    # 4 3 2 1 0
    # testHead.reverseIteratively(testHead)
    testHead.reverseRecursively(testHead)
    print("List after reversal: ")
    testTail.printList()
    # testTail.reverseIteratively(testTail)
    testTail.reverseRecursively(testTail)
    testHead.printList()
    # 0 1 2 3 4
