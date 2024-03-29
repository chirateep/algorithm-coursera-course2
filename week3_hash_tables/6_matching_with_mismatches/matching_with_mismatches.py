# python2

import sys
from collections import namedtuple

m1 = 1000000007
m2 = 1000000009
x = 1121044

Answer = namedtuple('answer_type', 'i j len')


def solve(k, text, pattern):
    result = []
    for i in range(len(text) - len(pattern) + 1):
        s = t[i: i + len(pattern)]
        for _ in range(k):
            max_substring = 0
            found = False
            left = 0
            right = len(pattern)
            while(left <= right):
                mid = (left + right) // 2
                if s[:mid] == pattern[:mid]:
                    found = True
                    max_substring = mid

                if found:
                    left = mid + 1
                    found = False
                else:
                    right = mid - 1

            if max_substring == len(pattern):
                break
            pos = max_substring
            s = s[:pos] + pattern[pos] + s[pos+1:]
        if pattern == s:
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
    # print(h1_pre)
    # print(h2_pre)
    # print(a, l, a + l)
    h1 = ((h1_pre[a + l] % m1) - (pow(x, l, m1) * (h1_pre[a] % m1))) % m1
    h2 = ((h2_pre[a + l] % m2) - (pow(x, l, m2) * (h2_pre[a] % m2))) % m2
    return h1, h2


for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    format_ans = '{0}'.format(len(ans))
    for x in ans:
        format_ans += ' {0}'.format(x)
    print(format_ans)
