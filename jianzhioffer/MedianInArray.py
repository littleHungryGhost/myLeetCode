# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.max = []
        self.min = []

    def MaxInsert(self, num):
        self.max.append(num)
        n = len(self.max)
        s = n-1
        i = (s-1)/2
        while i >= 0:
            if num > self.max[i]:
                self.max[s] = self.max[i]
                s = i
                i = (i-1)/2
            else:
                break
        self.max[s] = num
    def MinInsert(self, num):
        self.min.append(num)
        n = len(self.min)
        s = n-1
        i = (s-1)/2
        while i >= 0:
            if num < self.min[i]:
                self.min[s] = self.min[i]
                s = i
                i = (i-1)/2
            else:
                break
        self.min[s] = num
    def MaxPop(self):
        num = self.max[0]
        self.max[0] = self.max[-1]
        self.max.pop()
        temp = self.max[0]
        n = len(self.max)
        s = 0
        i = 2*s+1
        while i < n:
            if i < n-1 and self.max[i] < self.max[i + 1]:
                i += 1
            if temp >= self.max[i]:
                break
            self.max[s] = self.max[i]
            s = i
            i = 2 * i + 1
        self.max[s] = temp
        return num
    def MinPop(self):
        num = self.min[0]
        self.min[0] = self.min[-1]
        self.min.pop()
        temp = self.min[0]
        n = len(self.min)
        s = 0
        i = 2*s+1
        while i < n:
            if i < n-1 and self.min[i] > self.min[i + 1]:
                i += 1
            if temp <= self.min[i]:
                break
            self.min[s] = self.min[i]
            s = i
            i = 2 * i + 1
        self.min[s] = temp
        return num
    def Insert(self, num):
        # write code here
        if (len(self.max)+len(self.min))&1 == 0:
            if self.min and num > self.min[0]:
                self.MinInsert(num)
                num = self.MinPop()
            self.MaxInsert(num)
        else:
            if self.max and num < self.max[0]:
                self.MaxInsert(num)
                num = self.MaxPop()
            self.MinInsert(num)

    def GetMedian(self, n=None):
        # write code here
        n = len(self.max)+len(self.min)
        if n == 0:
            return -1
        if n & 1 == 0:
            res = (self.max[0]+self.min[0])/2.0
        else:
            res = self.max[0]
        return res


if __name__ == '__main__':
    s = Solution()
    a = [5,2,3,4,1,6,7,0,8]
    for i in a:
        s.Insert(i)
        print s.GetMedian()
