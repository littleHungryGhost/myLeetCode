# coding=utf-8
def digitAtIndex(index):
    if index < 0:
        return -1
    elif index < 10:
        return index
    index -= 10
    digit = 2
    while True:
        num = countNumDigit(digit)
        if index <= num:
            return digitAtIndex2(index, digit)
        else:
            index -= num
            digit += 1

def countNumDigit(bit):
    # 某一位数的数量
    if bit < 1:
        return 0
    elif bit == 1:
        return 10
    else:
        return 9 * 10 ** (bit-1)
def beginOfDigit(digit):
    if digit == 1:
        return 0
    return 10**(digit-1)
def digitAtIndex2(index, digit):
    begin = beginOfDigit(digit)
    num = begin + index/digit
    bit = index % digit
    return int(str(num)[bit])

if __name__ == '__main__':
    print digitAtIndex(19)
