#coding=utf-8
def insetSort(input_list):
    pass
def stackSort(input_list):
    """堆排序"""
    n = len(input_list)
    i = (n-1)/2
    while i >= 0:
        heapAdjust(input_list, i, n)
        i -= 1
    i = n
    while i > 0:
        temp = input_list[0]
        input_list[0] = input_list[i-1]
        input_list[i-1] = temp
        heapAdjust(input_list, 0, i-1)
        i -= 1
def heapAdjust(L, s, n):
    temp = L[s]
    i = s*2+1
    while i < n:
        if i < n-1 and L[i] < L[i+1]:
            i += 1
        if temp > L[i]:
            break
        L[s] = L[i]
        s = i
        i = 2*i+1
    L[s] = temp

if __name__ == '__main__':
    a = [5,12,4,2,7,9,10,1]
    stackSort(a)
    print a