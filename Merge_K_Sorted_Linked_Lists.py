"""
You are given an array of k sorted singly linked lists.
Merge the linked lists into a single sorted linked list and return it.

"""


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    k = len(lists)
    ans = Node('!')
    res = ans
    tmp = 1
    while True:
        min_num = 999999999999 # assume maximum
        ind = -1
        for i, elem in enumerate(lists):
            if elem is not None and elem.val < min_num:
                ind = i
                min_num = elem.val
        if ind == -1:
            break
        ans.next = Node(min_num)
        ans = ans.next
        lists[ind] = lists[ind].next
    tmp = res.next
    del res
    return tmp


if __name__ == "__main__":
    a = Node(1, Node(3, Node(5)))
    b = Node(2, Node(4, Node(6)))
    c = Node(-1, Node(4, Node(9)))
    print(merge([a, b]))
    # 123456
    print(merge([a, b, c]))
    # -112344569
