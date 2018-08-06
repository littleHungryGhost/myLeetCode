# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return None
        n = len(rotateArray)
        if n == 1:
            return rotateArray[0]
        i = 0
        j = n-1
        while i < j:
            if j-i == 1:
                return rotateArray[j]
            med = (j+i)/2
            if rotateArray[i] == rotateArray[j] and rotateArray[i] == rotateArray[med]:
                return self.sequentialFind(rotateArray)
            if rotateArray[med] >= rotateArray[0]:
                i = med
            else:
                j = med
    def sequentialFind(self,rotateArray):
        n = len(rotateArray)
        min = rotateArray[0]
        i = 1
        while i<n:
            if rotateArray[i] < min:
                min = rotateArray[i]
            i += 1
        return min

if __name__ == '__main__':
    s = Solution()
    print s.minNumberInRotateArray(None)
