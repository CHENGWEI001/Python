https://www.lintcode.com/problem/k-closest-points/description?_from=ladder&&fromId=1

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

def customPrint(self):
    return str("%d, %d"%(self.x,self.y))

Point.__str__ = customPrint

def dist(pt, origin):
    return math.pow(pt.x - origin.x, 2) + math.pow(pt.y - origin.y, 2)

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    
    
    def kClosest(self, points, origin, k):
        # points.sort(key=lambda pt: math.pow(pt.x - origin.x, 2) + math.pow(pt.x - origin.y, 2))
        points.sort(key=lambda pt: (dist(pt, origin), pt.x, pt.y))
        k = min(k, len(points))
        # for p in points:
        #     print(p)
        return points[:k]
