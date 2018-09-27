# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        i = 0
        n = len(sequence)
        root = sequence[-1]
        while i < n-1:
            if sequence[i] > root:
                break
            i += 1
        j = i
        while j < n-1:
            if sequence[j] < root:
                return False
            j += 1
        left = right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < n-1:
            right = self.VerifySquenceOfBST(sequence[i:n-1])
        return left and right

if __name__ == '__main__':
    s = Solution()
    print s.VerifySquenceOfBST(None)
