# python3
_prime = 1000000007
x = 1


def _hash_func(s):
    ans = 0
    for c in s:
        ans = (ans * x + ord(c)) % _prime
    return ans


def _precompute_hash(t, p):
    h = [0] * (len(t) - len(p) + 1)
    # print(h)
    s = t[len(t) - len(p): len(t)]
    # print(s)
    h[len(t) - len(p)] = _hash_func(s)
    # print(h)

    for i in range(len(t) - len(p) - 1, -1, -1):
        h[i] = ((x * h[i+1]) + ord(t[i]) -
                ((x ** len(p)) * ord(t[i + len(p)]))) % _prime
    return h


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    result = []
    p_hash = _hash_func(pattern)
    # print(p_hash)
    h = _precompute_hash(text, pattern)
    # print(h)
    for i in range(len(text) - len(pattern) + 1):
        # print(i, h[i])
        if p_hash != h[i]:
            continue
        # print(text[i: i + len(pattern)])
        if text[i: i + len(pattern)] == pattern:
            result.append(i)
    # return [
    #     i
    #     for i in range(len(text) - len(pattern) + 1)
    #     if text[i:i + len(pattern)] == pattern
    # ]
    # print(result)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
