# python3
import sys

m1 = 1000000007
m2 = 1000000009
x = 1124410


class Solver:
    def __init__(self, s):
        self.s = s
        self.h1, self.h2 = self.precompute_hash()

    def precompute_hash(self):

        h1 = [0] * (len(self.s) + 1)
        h2 = [0] * (len(self.s) + 1)
        # print(h1, h2)
        for i in range(1, len(self.s) + 1):
            # print(i)
            # print(s[i])
            h1[i] = ((x * h1[i-1]) + ord(self.s[i-1])) % m1
            h2[i] = ((x * h2[i-1]) + ord(self.s[i-1])) % m2
        return h1, h2

    def hash_value(self, a, b, l):
        # print(self.h1, self.h2)
        # print(a + l)
        # print(b + l)
        ans1 = (self.h1[a + l] % m1) - (pow(x, l, m1) * (self.h1[a] % m1))
        ans2 = (self.h1[b + l] % m1) - (pow(x, l, m1) * (self.h1[b] % m1))
        ans3 = (self.h2[a + l] % m2) - (pow(x, l, m2) * (self.h2[a] % m2))
        ans4 = (self.h2[b + l] % m2) - (pow(x, l, m2) * (self.h2[b] % m2))
        return ans1, ans2, ans3, ans4

    def ask(self, a, b, l):
        ans1, ans2, ans3, ans4 = self.hash_value(a, b, l)
        # print(ans1, ans2, ans3, ans4)
        return ((ans1 % m1) == (ans2 % m1)) and ((ans3 % m2) == (ans4 % m2))


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, length = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, length) else "No")
