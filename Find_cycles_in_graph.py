"""
Given an undirected graph, determine if a cycle exists in the graph.
"""


class Solution:
    def __init__(self):
        self.storage = set()

    def find_cycle(self, graph):
        check = False
        for i in graph:
            if i in self.storage:
                return True
            self.storage.add(i)
            check = check or self.find_cycle(graph[i])
            if check is True:
                return True
        return check


if __name__ == "__main__":
    graph = {
        'a': {'a2': {}, 'a3': {}},
        'b': {'b2': {}},
        'c': {}
    }
    print(Solution().find_cycle(graph))
    # False
    graph['c'] = graph
    print(Solution().find_cycle(graph))
    # True
