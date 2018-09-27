# coding=utf-8
#最长不含重复字符的子字符串
def getLongestSubStr(string):
    if not string:
        return None
    position = [-1 for i in range(26)]
    cur_length = max_length = 0
    n = len(string)
    index = 0
    i = 0
    while i < n:
        pre = position[ord(string[i])-ord('a')]
        if i - pre > cur_length:
            cur_length += 1
        else:
            if cur_length > max_length:
                max_length = cur_length
            cur_length = i - pre
            index = pre + 1
        position[ord(string[i])-ord('a')] = i
        i += 1
    if cur_length > max_length:
        max_length = cur_length
    return string[index:index+max_length], max_length

if __name__ == '__main__':
    a="arabcacfr"
    print getLongestSubStr(a)