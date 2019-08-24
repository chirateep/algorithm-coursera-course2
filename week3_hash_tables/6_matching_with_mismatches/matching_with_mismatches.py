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
        # s = t[i: i + len(pattern)]
        pos_mismatch = 0
        # print('s first', text[i: i + len(pattern)])
        # print('p first', pattern)
        # print('i', i)
        for _ in range(k):
            max_substring = 0
            found = False
            left = 0
            right = len(pattern) - pos_mismatch
            while(left <= right):
                mid = (left + right) // 2
                # print('mid', mid)
                s_h1, s_h2 = hash_value(t_h1_pre, t_h2_pre,
                                        pos_mismatch + i, mid)
                p_h1, p_h2 = hash_value(p_h1_pre, p_h2_pre,
                                        pos_mismatch, mid)
                # if s[:mid] == pattern[:mid]:
                #     found = True
                #     max_substring = mid
                if s_h1 == p_h1 and s_h2 == p_h2:
                    found = True
                    max_substring = mid

                if found:
                    left = mid + 1
                    found = False
                else:
                    right = mid - 1

            pos_mismatch += max_substring + 1
            if max_substring >= len(pattern):
                pos_mismatch = len(pattern)
                break
            if pos_mismatch >= len(pattern) or pos_mismatch >= len(text):
                pos_mismatch = len(pattern)
                break
            # print('max', max_substring)
            # print('pos', pos_mismatch)
            # s = s[:pos] + pattern[pos] + s[pos+1:]
        # print('last pos', pos_mismatch)
        # print(len(pattern) - pos_mismatch)
        s_h1, s_h2 = hash_value(t_h1_pre, t_h2_pre, i + pos_mismatch,
                                len(pattern) - pos_mismatch)
        p_h1, p_h2 = hash_value(p_h1_pre, p_h2_pre, pos_mismatch,
                                len(pattern) - pos_mismatch)
        if s_h1 == p_h1 and s_h2 == p_h2:
            result.append(i)
        # print('-------------')
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
    print(len(ans), *ans)
