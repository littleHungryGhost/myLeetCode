class Solution(object):
    # def convert(self, s, numRows):
    #     """
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """
    #     root = []
    #     tree = {}
    #     root.append(0)
    #     i = 0
    #     limit = numRows*2-2
    #     while i < len(s)-1:
    #         while i < limit and i<len(s)-1:
    #             while i<limit-numRows+1 and i<len(s)-1:
    #                 if tree.has_key(i):
    #                     tree[i].append(i+1)
    #                 else:
    #                     tree[i] = [i+1,]
    #                 i += 1
    #             if i<len(s)-1:
    #                 tree[i+1] = []
    #                 i += 1
    #             while i<limit and i<len(s)-1:
    #                 tree[i+1] = [i,]
    #                 i += 1
    #         if i<len(s)-1:
    #             root.append(i)
    #             limit = i + numRows*2-2
    #     print tree
    #     result = ""
    #     while root:
    #         p = root.pop(0)
    #         print p
    #         result += s[p]
    #         if tree.has_key(p):
    #             root += tree[p]
    #     return result
    def convert(self, s, numRows):
        if numRows==1 or numRows>=len(s):
            return s
        row, direction, res = 0, -1, [""]*numRows
        for char in s:
            res[row] += char
            if row==0 or row == numRows-1:
                direction *= -1
            row += direction
        return "".join(res)

if __name__ == '__main__':
    s = Solution()
    print s.convert("PAYPALISHIRING",4)