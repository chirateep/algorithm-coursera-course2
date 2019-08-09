# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job
        print(next_free_time)

    return result


def fast_assign_jobs(n_workers, jobs):
    result = []
    next_free_time = []
    for i in range(n_workers):
        val = (0, i)
        next_free_time.append(val)

    heapq.heapify(next_free_time)

    for job in jobs:
        next_worker = heapq.heappop(next_free_time)
        result.append(AssignedJob(next_worker[1], next_worker[0]))
        heapq.heappush(next_free_time, (next_worker[0] + job, next_worker[1]))
        # print(next_free_time)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = fast_assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
