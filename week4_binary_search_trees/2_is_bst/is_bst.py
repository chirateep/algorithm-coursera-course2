#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


key = []
left = []
right = []
result = []


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    is_binary = True
    for i in range(len(tree)):
        key.append(tree[i][0])
        left.append(tree[i][1])
        right.append(tree[i][2])

    if len(tree) > 0:
        _inOrderRecursive(0)

    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            is_binary = False
    return is_binary


def _inOrderRecursive(root):
    if root == -1:
        return
    _inOrderRecursive(left[root])
    result.append(key[root])
    _inOrderRecursive(right[root])


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
