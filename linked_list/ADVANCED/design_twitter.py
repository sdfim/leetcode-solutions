# Design Twitter
# Problem: https://leetcode.com/problems/design-twitter/
# Solution:

from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list:
        heap = []
        for user in self.following[userId] | {userId}:
            for tweet in self.tweets[user]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        return [tweetId for _, tweetId in sorted(heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

if __name__ == "__main__":
    # Example use case
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # [6, 5]
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # [5]
