"""
Implement a queue class using two stacks. A queue is a data structure that supports
the FIFO protocol (First in = first out). Your class should support the enqueue and
dequeue methods like a standard queue.
"""


class Queue:  # O(1) push, O(1) Amortized pop
    def __init__(self):
        self.__stack0 = []
        self.__stack1 = []

    def enqueue(self, val):
        self.__stack0.append(val)

    def dequeue(self):
        if not self.__stack1:
            while self.__stack0:
                self.__stack1.append(self.__stack0.pop())
        return self.__stack1.pop()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    # 1 2 3
