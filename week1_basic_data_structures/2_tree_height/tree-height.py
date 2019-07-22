# python3

import sys
import threading
from collections import namedtuple

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

Node = namedtuple("Node", ["value", "height"])


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight

    def build_tree(self):
        node_list = list()
        root_index = -1
        for i in range(self.n):
            init_list = list()
            node_list.append(init_list[:])
        for i in range(self.n):
            if self.parent[i] == -1:
                root_index = i
            else:
                node_index = self.parent[i]
                node_list[node_index].append(i)
        self.tree = node_list
        self.root = root_index

    def fast_compute_height(self):
        queue = list()
        height = 1
        node_root = Node(self.root, height)
        queue.append(node_root)
        while len(queue) > 0:
            # print(queue)
            node_current = queue.pop(0)
            for node_value in self.tree[node_current.value]:
                node = Node(node_value, node_current.height + 1)
                queue.append(node)

        return node_current.height


def main():
    tree = TreeHeight()
    tree.read()
    tree.build_tree()
    # print(tree.compute_height())
    print(tree.fast_compute_height())


threading.Thread(target=main).start()
