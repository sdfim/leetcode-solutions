# Design Exam Scores Tracker
# Problem: https://leetcode.com/problems/design-exam-scores-tracker/

import bisect

class ExamTracker:

    def __init__(self):
        self.times = []
        self.prefix_scores = [0]
        self.current_total = 0

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.current_total += score
        self.prefix_scores.append(self.current_total)

    def totalScore(self, startTime: int, endTime: int) -> int:
        # Find first index >= startTime
        # Find first index > endTime (to define range [start, end])
        
        idx_start = bisect.bisect_left(self.times, startTime)
        idx_end = bisect.bisect_right(self.times, endTime) 
        
        # Valid range in 'times': [idx_start, idx_end-1]
        # In prefix_scores:
        # Sum from idx_start to idx_end-1 is prefix_scores[idx_end] - prefix_scores[idx_start]
        
        # Note: prefix_scores has length len(times) + 1.
        # prefix_scores[0] = 0
        # prefix_scores[1] corresponds to sum of times[0]
        # prefix_scores[k] corresponds to sum of times[0...k-1]
        
        # We need sum of times[idx_start ... idx_end-1].
        # Sum(0...idx_end-1) - Sum(0...idx_start-1)
        # = prefix_scores[idx_end] - prefix_scores[idx_start]
        
        # Handing bounds:
        if idx_start >= len(self.times):
            return 0
        if idx_start >= idx_end:
            return 0
            
        return self.prefix_scores[idx_end] - self.prefix_scores[idx_start]

if __name__ == "__main__":
    tracker = ExamTracker()
    tracker.record(1, 80)
    tracker.record(3, 90)
    tracker.record(5, 100)
    print(tracker.totalScore(1, 3)) # 170
    print(tracker.totalScore(2, 5)) # 190
