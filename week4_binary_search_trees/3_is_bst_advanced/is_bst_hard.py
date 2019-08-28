#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

key = []
left = []
right = []
result = []
side_tree = []
high_tree = []


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    is_binary = True
    for i in range(len(tree)):
        key.append(tree[i][0])
        left.append(tree[i][1])
        right.append(tree[i][2])

    if len(tree) > 0:
        _inOrderRecursive(0, 'm', 0)

    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            is_binary = False

        if result[i] == result[i + 1]:
            # print(i)
            if side_tree[i] == 'l' and high_tree[i] > high_tree[i + 1]:
                # print(i)
                is_binary = False
        # print(result[i], side_tree[i], high_tree[i])
    return is_binary


def _inOrderRecursive(root, side, high):
    if root == -1:
        return
    _inOrderRecursive(left[root], 'l', high + 1)
    result.append(key[root])
    side_tree.append(side)
    high_tree.append(high)
    _inOrderRecursive(right[root], 'r', high + 1)


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
