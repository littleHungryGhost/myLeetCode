# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        rows = len(array)
        cols = len(array[0])
        if rows <= 0 or cols <= 0:
            return False
        i = 0
        j = cols - 1
        while i < rows and j >= 0:
            if target > array[i][j]:
                i += 1
            elif target < array[i][j]:
                j -= 1
            else:
                return True
        return False
if __name__ == '__main__':
    s = Solution()
    a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print s.Find(13,None)
