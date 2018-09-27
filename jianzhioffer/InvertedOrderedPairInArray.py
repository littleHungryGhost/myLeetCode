# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0
        copy = [i for i in data]
        res = self.Divide(data, copy, 0, len(data)-1)
        return res

    def Divide(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        mid = (start+end)/2
        count = 0
        left = self.Divide(copy, data, start, mid)
        right = self.Divide(copy, data, mid+1, end)
        i = mid
        k = j = end
        while i >= start and j >= mid+1:
            if data[i] > data[j]:
                count += j - mid
                copy[k] = data[i]
                i -= 1
            else:
                copy[k] = data[j]
                j -= 1
            k -= 1
        while i >= start:
            copy[k] = data[i]
            i -= 1
            k -= 1
        while j >= mid+1:
            copy[k] = data[j]
            j -= 1
            k -= 1
        res = left+right+count
        while res > 1000000007:
            res -= 1000000007
        return res

if __name__ == '__main__':
    s = Solution()
    print s.InversePairs([7,5,6,4])



