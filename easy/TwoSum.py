class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = j = 0
        l = len(nums)
        while(i<l):
            j = i+1
            while(j<l):
                if target==nums[i]+nums[j]:
                    return [i,j]
                j += 1
            i += 1
    def twoSum2(self,nums,target):
        hm = {}
        for i,j in enumerate(nums):
            n = target-nums[i]
            if n in hm:
                return [hm[n],i]
            else:
                hm[j]=i

if __name__ == '__main__':
    s = Solution()
    print s.twoSum2([2,5,7,9],9)