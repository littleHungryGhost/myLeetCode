# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
import math
import collections
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        points = [(i.x, i.y) for i in points]
        points = list(collections.Counter(points).items())
        res = max([i[1] for i in points])
        fix_dict = {}
        for i in range(len(points)):
            temp_dict = {}
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i+1, len(points)):
                x2 = points[j][0]
                y2 = points[j][1]
                k = (y1-y2)/

if __name__ == '__main__':
    s = Solution()
    points = []
    for i in range(10):
        p = Point(i, i+1)
        points.append(p)
    points.append(Point(1,2))
    s.maxPoints(points)
