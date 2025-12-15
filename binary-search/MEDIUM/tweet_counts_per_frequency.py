# Tweet Counts Per Frequency
# Problem: https://leetcode.com/problems/tweet-counts-per-frequency/

from typing import List
import bisect
import collections

class TweetCounts:

    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            delta = 60
        elif freq == "hour":
            delta = 3600
        else: # day
            delta = 86400
            
        times = self.tweets[tweetName]
        res = []
        
        curr = startTime
        while curr <= endTime:
            end = min(curr + delta, endTime + 1)
            # Find counts in [curr, end)
            # Ideally [curr, min(curr+delta, endTime+1)).
            # Problem says chunks are [startTime, startTime + delta), etc.
            # Last chunk may be smaller.
            
            idx1 = bisect.bisect_left(times, curr)
            idx2 = bisect.bisect_left(times, end)
            
            res.append(idx2 - idx1)
            curr += delta
            
        return res

if __name__ == "__main__":
    obj = TweetCounts()
    obj.recordTweet("tweet3", 0)
    obj.recordTweet("tweet3", 60)
    obj.recordTweet("tweet3", 10)
    print(obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 59))  # [2]
    print(obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 60))  # [2, 1]
