#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


key = []
left = []
right = []


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    is_binary = True
    for i in range(len(tree)):
        key.append(tree[i][0])
        left.append(tree[i][1])
        right.append(tree[i][2])

    for i in range(len(tree)):
        find_pos = find(key[i], 0)
        if find_pos == i:
            continue
        else:
            is_binary = False
            return
    return is_binary


def find(k, root):
    if key[root] == k:
        return root
    elif key[root] > k:
        if left[root] != -1:
            return find(k, left[root])
        return root
    elif key[root] < k:
        if right[root] != -1:
            return find(k, right[root])
        return root


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
