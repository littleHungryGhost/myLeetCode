# coding=utf-8
def Combine(ss):
    result = []
    for i in range(1, len(ss)+1):
        CombinationRecurse(ss, i, "", result)
    return result

def CombinationRecurse(ss, m, comb, result):
    if len(ss) == m:
        result.append(comb+ss)
        return
    if m == 0:
        result.append(comb)
        return
    if len(ss) < m or len(ss) == 0:
        return
    if len(ss) > 0:
        CombinationRecurse(ss[1:], m - 1, comb + ss[0], result)
        CombinationRecurse(ss[1:], m, comb, result)

if __name__ == '__main__':
    print Combine("abc")