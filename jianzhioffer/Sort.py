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

def MergeSort(array):
    """归并排序"""
    if not array:
        return None
    Divide(array, array, 0, len(array)-1)
    return array
def Divide(array1, array2, start, end):
    temp = [0 for i in range(end+1)]
    if start == end:
        array2[start] = array1[start]
    else:
        mid = (start+end)/2
        Divide(array1, temp, start, mid)
        Divide(array1, temp, mid+1, end)
        Merge(temp, array2, start, mid, end)
def Merge(array1, array2, start, mid, end):
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        if array1[i] < array1[j]:
            array2[k] = array1[i]
            i += 1
        else:
            array2[k] = array1[j]
            j += 1
        k += 1
    while i <= mid:
        array2[k] = array1[i]
        k += 1
        i += 1
    while j <= end:
        array2[k] = array1[j]
        j += 1
        k += 1
def MergeSort2(array):
    n = len(array)
    temp = [0 for i in range(n)]
    interval = 1
    while interval < n:
        DivideAndMerge(array, temp, interval, n)
        interval *= 2
        DivideAndMerge(temp, array, interval, n)
        interval *= 2
    return array
def DivideAndMerge(array1, array2, interval, n):
    i = 0
    while n-i >= 2*interval:
        Merge(array1, array2, i, i+interval-1, i+2*interval-1)
        i = i + 2*interval
    if n-i > interval:
        Merge(array1, array2, i, i+interval-1, n-1)
    else:
        while i < n:
            array2[i] = array1[i]
            i += 1
if __name__ == '__main__':
    a = [5,12,4,2,7,9,10,1]
    # stackSort(a)
    # print a
    print MergeSort2(a)
