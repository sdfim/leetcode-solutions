# Find Minimum Time to Finish All Jobs
# Problem: https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
# Solution:

from typing import List

def minimumTimeRequired(jobs: List[int], k: int) -> int:
    def backtrack(index):
        if index == len(jobs):
            return max(workloads)

        min_time = float("inf")
        for i in range(k):
            if workloads[i] == 0:
                workloads[i] += jobs[index]
                min_time = min(min_time, backtrack(index + 1))
                workloads[i] -= jobs[index]
                break

            workloads[i] += jobs[index]
            min_time = min(min_time, backtrack(index + 1))
            workloads[i] -= jobs[index]

        return min_time

    jobs.sort(reverse=True)
    workloads = [0] * k
    return backtrack(0)

if __name__ == "__main__":
    jobs = [3, 2, 3]
    k = 3
    print(minimumTimeRequired(jobs, k))
