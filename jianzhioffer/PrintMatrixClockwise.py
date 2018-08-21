# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        result = []
        while start * 2 < rows and start * 2 < cols:
            self.printOneCricle(matrix, start, result)
            start += 1
        return result

    def printOneCricle(self, matrix, start, result):
        rows = len(matrix)
        cols = len(matrix[0])
        endx = cols - 1 - start
        endy = rows - 1 - start
        i = start
        while i <= endx:
            num = matrix[start][i]
            result.append(num)
            i += 1
        if start < endy:
            i = start + 1
            while i <= endy:
                num = matrix[i][endx]
                result.append(num)
                i += 1
        if start < endx and start < endy:
            i = endx - 1
            while i >= start:
                num = matrix[endy][i]
                result.append(num)
                i -= 1
        if start < endx and start < endy - 1:
            i = endy - 1
            while i > start:
                num = matrix[i][start]
                result.append(num)
                i -= 1

    def printMatrix2(self, matrix):
        # write code here
        if not matrix:
            return []
        re = []
        while True:
            re += matrix[0]
            matrix.pop(0)
            if not matrix:
                break
            matrix = zip(*matrix)[::-1]
        return re


if __name__ == '__main__':
    s = Solution()
    # a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    a = [[1,2],[3,4],[5,6]]
    print s.printMatrix(a)
    print s.printMatrix2(a)
