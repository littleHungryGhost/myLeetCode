#coding=utf-8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        通过异或操作来去除重复数字。best！
        """
        return reduce(lambda ret,i:ret^i,nums,0)

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1,2,3,3,1,2,4])