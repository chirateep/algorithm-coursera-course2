# python3
from collections import deque


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def max_sliding_window_fast(sequence, m):
    maximums = []
    windows_queue = deque()
    max_queue = deque()
    for i in range(m):
        number = sequence[i]
        windows_queue.append(number)

        if len(max_queue) == 0:
            max_queue.append(number)
        else:
            while max_queue[len(max_queue) - 1] < number:
                max_queue.pop()
                if len(max_queue) == 0:
                    break
            max_queue.append(number)
    maximums.append(max_queue[0])

    for i in range(len(sequence) - m):
        number = sequence[i+m]
        popleft = windows_queue.popleft()
        windows_queue.append(number)

        if popleft == max_queue[0]:
            max_queue.popleft()

        if len(max_queue) == 0:
            max_queue.append(number)
        else:
            while max_queue[len(max_queue) - 1] < number:
                max_queue.pop()
                if len(max_queue) == 0:
                    break
            max_queue.append(number)
        maximums.append(max_queue[0])

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(" ".join(map(str, max_sliding_window_fast(input_sequence,
                                                    window_size))))
