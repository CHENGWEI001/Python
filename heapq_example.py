# https://www.jiuzhang.com/solution/k-closest-points/#tag-highlight-lang-python

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

import heapq

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        self.heap = []
        for p in points:
            dist = (p.x - origin.x)**2 + (p.y - origin.y)**2
            heapq.heappush(self.heap, (-dist, -p.x, -p.y))
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        ans = []
        while len(self.heap):
            _, x, y = heapq.heappop(self.heap)
            ans.append(Point(-x, -y))
        return self.reverse(ans)
    
    def reverse(self, nums):
        start = 0
        end = len(nums)-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
