# python3

import sys

m1 = 1000000007
m2 = 1000000009
x = 1121044


def solve(k, text, pattern):
    result = []
    p_h1_pre, p_h2_pre = precompute_hash(pattern)
    t_h1_pre, t_h2_pre = precompute_hash(text)
    for i in range(len(text) - len(pattern) + 1):
        p_h1, p_h2 = hash_value(p_h1_pre, p_h2_pre, 0, len(pattern))
        t_h1, t_h2 = hash_value(t_h1_pre, t_h2_pre, i, len(pattern))
        if p_h1 == t_h1 and p_h2 == t_h2:
            result.append(i)
    return result


def precompute_hash(s):
    h1 = [0] * (len(s) + 1)
    h2 = [0] * (len(s) + 1)
    # print(h1, h2)
    for i in range(1, len(s) + 1):
        h1[i] = ((x * h1[i-1]) + ord(s[i-1])) % m1
        h2[i] = ((x * h2[i-1]) + ord(s[i-1])) % m2
    return h1, h2


def hash_value(h1_pre, h2_pre, a, l):
    # print(a, l)
    h1 = ((h1_pre[a + l] % m1) - (pow(x, l, m1) * (h1_pre[a] % m1))) % m1
    h2 = ((h2_pre[a + l] % m2) - (pow(x, l, m2) * (h2_pre[a] % m2))) % m2
    return h1, h2


for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)
