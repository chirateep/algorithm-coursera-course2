# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        if len(self.finish_time) == 0:
            left_pop = 0
        else:
            left_pop = lower_pop(self.finish_time, request.arrived_at)

        # print('pop', count_pop)
        self.finish_time = self.finish_time[left_pop:]

        if len(self.finish_time) == 0:
            start_time = request.arrived_at
        else:
            last_element = len(self.finish_time)
            start_time = max(self.finish_time[last_element - 1],
                             request.arrived_at)

        finish_time = start_time + request.time_to_process
        # print('fin time', finish_time)

        if len(self.finish_time) < self.size:
            self.finish_time.append(finish_time)
        else:
            return Response(True, -1)

        # print(self.finish_time)

        return Response(False, start_time)


def lower_pop(a, x):
    lower = list()
    left, right = 0, len(a)

    if (a[left] > x):
        return len(lower)

    if (a[right-1] <= x):
        return len(a)

    while (left <= right):
        mid = (left + right) // 2

        if (a[mid] <= x):
            lower += a[left:mid+1]
            left = mid + 1
        else:
            right = mid - 1

    return len(lower)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
