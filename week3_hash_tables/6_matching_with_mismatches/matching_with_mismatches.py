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
        for _ in range(k):
            max_substring = Answer(0, 0, 0)
            s_h1_pre = t_h1_pre[i: i + len(pattern) + 1]
            s_h2_pre = t_h2_pre[i: i + len(pattern) + 1]
            # print(s_h1_pre)
            found = False
            left = 0
            right = len(pattern)
            while(left <= right):
                mid = (left + right) // 2
                # print('mid', mid)
                s_h1_dict = dict()
                s_h2_dict = dict()
                for j in range(len(pattern) - mid + 1):
                    s_h1, s_h2 = hash_value(s_h1_pre, s_h2_pre, j, mid)
                    s_h1_dict[s_h1] = j
                    s_h2_dict[s_h2] = j

                for j in range(len(pattern) - mid + 1):
                    p_h1, p_h2 = hash_value(p_h1_pre, p_h2_pre, j, mid)

                    if s_h1_dict.get(p_h1) is None or s_h2_dict.get(p_h2) is None:
                        continue
                    else:
                        found = True
                        max_substring = Answer(s_h1_dict.get(p_h1), j, mid)
                        break

                if found:
                    left = mid + 1
                    found = False
                else:
                    right = mid - 1

            # print(max_substring)
            if max_substring.i != 0:
                pos_text = max_substring.i + i - 1
                pos_pattern = max_substring.j - 1
                text = text[:pos_text] + pattern[pos_pattern] + text[pos_text+1:]
            else:
                pos_text = max_substring.len + max_substring.i + i - 1
                pos_pattern = max_substring.len + max_substring.j - 1
                # print(text[pos_text])
                # print(pattern[pos_pattern])
                text = text[:pos_text] + pattern[pos_pattern] + text[pos_text+1:]
                # print(text)
            t_h1_pre, t_h2_pre = precompute_hash(text)

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
