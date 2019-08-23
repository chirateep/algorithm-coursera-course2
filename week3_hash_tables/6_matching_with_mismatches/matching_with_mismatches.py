# python3

import sys
from collections import namedtuple

m1 = 1000000007
m2 = 1000000009
x = 1121044

Answer = namedtuple('answer_type', 'i j len')


def solve(k, text, pattern):
    result = []
    p_h1_pre, p_h2_pre = precompute_hash(pattern)
    t_h1_pre, t_h2_pre = precompute_hash(text)
    for i in range(len(text) - len(pattern) + 1):
        s = t[i: i + len(pattern)]
        s_h1_pre = t_h1_pre[i: i + len(pattern) + 1]
        s_h2_pre = t_h2_pre[i: i + len(pattern) + 1]
        for _ in range(k):
            max_substring = Answer(0, 0, 0)
            # print(s_h1_pre)
            found = False
            left = 0
            right = len(pattern)
            # print(s_h1_pre, s_h2_pre)
            # print(p_h1_pre, p_h2_pre)
            while(left <= right):
                mid = (left + right) // 2
                # print('mid', mid)
                # print('s', s[0:mid])
                # print('p', p[0:mid])
                s_h1, s_h2 = hash_value(s_h1_pre, s_h2_pre, 0, mid)
                p_h1, p_h2 = hash_value(p_h1_pre, p_h2_pre, 0, mid)
                if s_h1 == p_h1 and s_h2 == p_h2:
                    found = True
                    max_substring = Answer(0, 0, mid)

                if found:
                    left = mid + 1
                    found = False
                else:
                    right = mid - 1

            # print(max_substring)
            if max_substring.len == len(pattern):
                break
            pos = max_substring.len
            # print('pos', pos)
            # print(s[pos])
            # print(pattern[pos])
            s = s[:pos] + pattern[pos] + s[pos+1:]
            # print('s', s)
            s_h1_pre, s_h2_pre = precompute_hash(s)
        p_h1, p_h2 = hash_value(p_h1_pre, p_h2_pre, 0, len(pattern))
        s_h1, s_h2 = hash_value(s_h1_pre, s_h2_pre, 0, len(s))
        if p_h1 == s_h1 and p_h2 == s_h2:
            # print('add')
            result.append(i)
        # print('==========')
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
