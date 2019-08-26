# python3

import sys
import threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self._inOrderRecursive(0)
        return self.result

    def _inOrderRecursive(self, root):
        if root == -1:
            return
        self._inOrderRecursive(self.left[root])
        self.result.append(self.key[root])
        self._inOrderRecursive(self.right[root])

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self._preOrderRecursive(0)
        return self.result

    def _preOrderRecursive(self, root):
        if root == -1:
            return
        self.result.append(self.key[root])
        self._preOrderRecursive(self.left[root])
        self._preOrderRecursive(self.right[root])

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self._postOrderRecursive(0)
        return self.result

    def _postOrderRecursive(self, root):
        if root == -1:
            return
        self._postOrderRecursive(self.left[root])
        self._postOrderRecursive(self.right[root])
        self.result.append(self.key[root])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
