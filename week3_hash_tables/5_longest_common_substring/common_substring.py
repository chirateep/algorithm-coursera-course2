# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

m1 = 1000000007
m2 = 1000000009
x = 1121044


def solve(s, t):
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
                    ans = Answer(i, j, l)
    return ans


def fast_solve(s, t):
    ans = Answer(0, 0, 0)
    # print('max_common', max_common_range)
    s_h1_pre, s_h2_pre = precompute_hash(s)
    t_h1_pre, t_h2_pre = precompute_hash(t)
    found = False
    left = 0
    right = len(s)
    while(left <= right):
        mid = (left + right) // 2

        s_h1_dict = dict()
        s_h2_dict = dict()
        for j in range(len(s) - mid + 1):
            # print('real_string', s[j:j+i])
            s_h1, s_h2 = hash_value(s_h1_pre, s_h2_pre, j, mid)
            s_h1_dict[s_h1] = j
            s_h2_dict[s_h2] = j
        # print(s_h1_dict)
        # print(s_h2_dict)
        for j in range(len(t) - mid + 1):
            # print('real_string', t[j:j+mid])
            t_h1, t_h2 = hash_value(t_h1_pre, t_h2_pre, j, mid)
            # print(t_h1, t_h2)
            if s_h1_dict.get(t_h1) is None or s_h2_dict.get(t_h2) is None:
                continue
            else:
                found = True
                ans = Answer(s_h1_dict.get(t_h1), j, mid)
                break

        if found:
            left = mid + 1
            found = False
        else:
            right = mid - 1

    return ans


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


def binary_search(a, x):
    left, right = 0, len(a)
    if a[left] > x or a[len(a) - 1] < x:
        return -1

    while(left <= right):
        mid = (left + right) // 2
        # print('mid', mid)
        if a[mid] == x:
            return mid

        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = fast_solve(s, t)
    print(ans.i, ans.j, ans.len)
