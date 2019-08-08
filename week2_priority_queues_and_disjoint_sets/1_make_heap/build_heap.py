# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def fast_build_heap(data):
    swaps = []
    size = len(data)
    for i in range(len(data) // 2, 0, -1):
        # siftdown(i-1)
        # print("first", i)
        min_index = -1
        while (i != min_index):
            min_index = i
            left = left_child(i)
            # print("left", left)
            if left <= size and data[left-1] < data[min_index-1]:
                min_index = left
            right = right_child(i)
            if right <= size and data[right-1] < data[min_index-1]:
                min_index = right

            if i == min_index:
                break
            else:
                swaps.append((i-1, min_index-1))
                data[i - 1], data[min_index-1] = data[min_index-1], data[i-1]
                i = min_index
                min_index = -1

            # print("data", data)
        # print(i)
    # print("data finish", data)
    return swaps


def parent(i):
    return (i + 1) // 2


def left_child(i):
    return (2 * i)


def right_child(i):
    return (2 * i) + 1


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = fast_build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
