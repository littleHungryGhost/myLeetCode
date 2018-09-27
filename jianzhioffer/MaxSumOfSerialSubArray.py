# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        i = 0
        n = len(array)
        sum = 0
        max = -0x80000000
        while i < n:
            if sum <= 0:
                sum = array[i]
            else:
                sum += array[i]
            if max < sum:
                max = sum
            i += 1
        return max

    def FindGreatestSumOfSubArray2(self, array):
        if not array:
            return 0
        max = -0x80000000
        return self.Recurse(array, max)[1]
    def Recurse(self,array, max):
        if len(array) == 1:
            return array[0], array[0]
        res, max = self.Recurse(array[:-1], max)
        if res <= 0:
            res = array[-1]
        else:
            res += array[-1]
        if max < res:
            max = res
        return res, max

if __name__ == '__main__':
    s = Solution()
    print s.FindGreatestSumOfSubArray2([1,-2,3,10,-4,7,2,-5])