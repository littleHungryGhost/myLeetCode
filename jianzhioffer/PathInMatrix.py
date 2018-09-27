class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or rows < 1 or cols < 1 or not path or len(path) > rows*cols:
            return False
        visited = [[0 for i in range(cols)] for i in range(rows)]
        if isinstance(matrix, list):
            i = 0
            while i < rows:
                j = 0
                while j < cols:
                    if self.verifyPath(matrix, rows, cols, i, j, path, visited):
                        return True
                    j += 1
                i += 1
            return False
        elif isinstance(matrix,str):
            i = 0
            while i < rows*cols:
                if self.verifyPath(matrix, rows, cols, i/cols, i%cols, path, visited):
                    return True
                i += 1
            return False


    def verifyPath(self, matrix, rows, cols, i, j, path, visited):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return False
        if isinstance(matrix, list):
            if matrix[i][j] == path[0] and visited[i][j] == 0:
                if len(path) == 1:
                    return True
                visited[i][j] = 1
                select = [[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
                for index in select:
                    flag = self.verifyPath(matrix, rows, cols, index[0], index[1], path[1:], visited)
                    if flag:
                        return flag
                visited[i][j] = 0
            else:
                return False
        elif isinstance(matrix,str):
            if matrix[i*cols+j] == path[0] and visited[i][j] == 0:
                if len(path) == 1:
                    return True
                visited[i][j] = 1
                select = [[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
                for index in select:
                    flag = self.verifyPath(matrix, rows, cols, index[0], index[1], path[1:], visited)
                    if flag:
                        return flag
                visited[i][j] = 0
            else:
                return False

if __name__ == '__main__':
    s = Solution()
    a = [['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
    b = "abtgcfcsjdeh"
    print s.hasPath("gdbabcdefgsd", 12, 1, 'abcdefgs')
