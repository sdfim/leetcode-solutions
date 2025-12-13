# Minimum Number of Work Sessions to Finish the Tasks
# Problem: https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
# Solution:

from typing import List

def minSessions(tasks: List[int], sessionTime: int) -> int:
    def backtrack(index):
        if index == len(tasks):
            return len(sessions)

        min_sessions = float("inf")
        for i in range(len(sessions)):
            if sessions[i] + tasks[index] <= sessionTime:
                sessions[i] += tasks[index]
                min_sessions = min(min_sessions, backtrack(index + 1))
                sessions[i] -= tasks[index]

        sessions.append(tasks[index])
        min_sessions = min(min_sessions, backtrack(index + 1))
        sessions.pop()

        return min_sessions

    sessions = []
    return backtrack(0)

if __name__ == "__main__":
    tasks = [1, 2, 3, 4, 5]
    sessionTime = 5
    print(minSessions(tasks, sessionTime))
