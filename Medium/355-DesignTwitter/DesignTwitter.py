from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.time = 0
        self.followDatabase = defaultdict(set)
        self.tweetDatabase = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetDatabase[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for tweet in self.tweetDatabase[userId]:
            heap.append(tweet)
        for user in self.followDatabase[userId]:
            for tweet in self.tweetDatabase[user]:
                heap.append(tweet)

        heapq.heapify(heap)
        res = []
        count = 0
        while heap and count < 10:
            res.append(heapq.heappop(heap)[1])
            count += 1
        return res

    """ More efficient way to fetch feeds.
     def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followDatabase[userId].add(userId)

        for user in self.followDatabase[userId]:
            if user in self.tweetDatabase:
                index = len(self.tweetDatabase[user]) - 1
                time, tweet = self.tweetDatabase[user][index]
                heap.append([time, tweet, user, index - 1])
        
        heapq.heapify(heap)
        while heap and len(res) < 10:
            time, tweet, user, index = heapq.heappop(heap)
            res.append(tweet)
            if index >= 0:
                time, tweet = self.tweetDatabase[user][index]
                heapq.heappush(heap, [time, tweet, user, index - 1])
        return res 
    """

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followDatabase[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followDatabase[followerId]:
            self.followDatabase[followerId].remove(followeeId)