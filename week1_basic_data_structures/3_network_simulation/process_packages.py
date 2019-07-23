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
            start_time = request.arrived_at
        else:
            last_element = len(self.finish_time)
            if request.arrived_at < self.finish_time[last_element - 1]:
                print('late')
                return Response(True, -1)

            start_time = max(self.finish_time[last_element - 1],
                             request.arrived_at)
            count_pop = 0
            for i in range(len(self.finish_time)):
                if self.finish_time[i] <= request.arrived_at:
                    count_pop += 1

            print('pop', count_pop)
            for i in range(count_pop):
                self.finish_time.pop(0)

        finish_time = start_time + request.time_to_process
        print('fin time', finish_time)

        if len(self.finish_time) < self.size:
            self.finish_time.append(finish_time)
        else:
            return Response(True, -1)

        print(self.finish_time)

        return Response(False, start_time)


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
