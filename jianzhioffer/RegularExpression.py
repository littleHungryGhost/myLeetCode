# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self,s, pattern):
        if s == None or pattern == None:
            return False
        return self.match_recurse(s, pattern)

    def match_recurse(self, s, pattern):
        if not s and not pattern:
            return True
        if s and not pattern:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if s and (pattern[0] == s[0] or pattern[0] == '.'):
                return self.match_recurse(s[1:], pattern[2:]) \
                       or self.match_recurse(s, pattern[2:]) \
                       or self.match_recurse(s[1:], pattern)
            else:
                return self.match_recurse(s, pattern[2:])
        elif s and (pattern[0] == s[0] or pattern[0] == '.'):
            return self.match_recurse(s[1:], pattern[1:])
        else:
            return False



if __name__ == '__main__':
    s = Solution()
    print s.match("aaa","ab*ac*a")