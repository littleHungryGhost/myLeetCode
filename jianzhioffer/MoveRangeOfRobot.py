# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visited = [[0 for i in range(cols)]for i in range(rows)]
        result = self.move(threshold, rows, cols, 0, 0, visited)
        return result

    def move(self, threshold, rows, cols, i, j, visited):
        if i < 0 or j < 0 or i >= rows or j >= cols or visited[i][j] == 1 or self.numSum(i)+self.numSum(j) > threshold:
            return 0
        visited[i][j] = 1
        result = 1
        select = [[i,j+1],[i,j-1],[i-1,j],[i+1,j]]
        for dir in select:
            result += self.move(threshold, rows, cols, dir[0], dir[1], visited)
        return result


    def numSum(self, num):
        result = 0
        while num/10 > 0:
            result += num%10
            num /= 10
        result += num
        return result

if __name__ == '__main__':
    s = Solution()
    print s.movingCount(5,10,1)
