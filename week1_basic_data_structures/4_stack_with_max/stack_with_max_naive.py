# python3
from collections import deque
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = deque()
        self.__max = -1

    def Push(self, a):
        self.__stack.append(a)
        if a > self.__max:
            self.__max = a

    def Pop(self):
        assert(len(self.__stack))
        pop = self.__stack.pop()
        if pop == self.__max:
            self.__max = -1
            for i in range(len(self.__stack)):
                left = self.__stack.popleft()
                if left > self.__max:
                    self.__max = left
                self.__stack.append(left)

    def Max(self):
        assert(len(self.__stack))
        return self.__max


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
