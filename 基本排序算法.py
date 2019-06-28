# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:30:14 2018

@author: Administrator
"""
#冒泡排序
def bubbleSort(mylist):
    length = len(mylist)
    for i in range(0,length):
        for j in range(length-i-1):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
    return mylist

#选择排序(1)
def selectSort(mylist):
    length = len(mylist)
    for i in range(0,length):
        min_index=i
        for j in range(i+1,length):
            if mylist[min_index]>mylist[j]:
                min_index=j
        mylist[i],mylist[min_index]=mylist[min_index],mylist[i]
    return mylist           
#选择排序(2)
def selectSort2(mylist):
    length= len(mylist)
    for i in range (length):
        for j in range(length-i):
            if mylist[i]>mylist[i+j]:
                mylist[i],mylist[i+j]=mylist[i+j],mylist[i] 
    return mylist

#快排
def quickSort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [ i for i  in array[1:] if i<=pivot]
        big =[j for j in array[1:] if j>pivot]    
        return quickSort(less)+[pivot]+quickSort(big)

#直接插入排序(Python 写法更优化)
def insertSort(mylist):
    length= len(mylist)
    for i in range(1,length):
        for j in range(i):
            if mylist[i]<mylist[j]:
                mylist.insert(j,mylist[i])
                mylist.pop(i+1)
                break
    return mylist   

#插入排序
def insertSort2(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key
    return array

#希尔排序 有点麻烦看不懂
def ShellSort(relist):
    n = len(relist)
    gap = int(n/2)  # 初始步长

    while gap > 0:
        for i in range(gap, n):
            temp = relist[i]   # 每个步长进行插入排序
            j = i
            # 插入排序
            while j >= gap and relist[j - gap] > temp:
                relist[j] = relist[j - gap]
                j -= gap
            relist[j] = temp

        gap = int(gap/2)  # 得到新的步长

    return relist

#print(ShellSort([1,5,2,6,9,3]))

"""归并排序"""
def mergesort(seq):
    if len(seq) <= 1:
        return seq
    mid = int( len(seq) / 2)  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left,right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result



seq = [5,3,0,6,1,4]
print ("Before:", seq)
result = mergesort(seq)
print ("After:",result)

#堆排序
def heap_sort(A):
    build_max_heap(A)
    for i in range(len(A)-1,-1,-1):
        A[i],A[0] = A[0],A[i]
        adjust_heap(A,i,0)
    return A

def build_max_heap(A):
    heap_size = len(A)
    for i in range(len(A)//2-1,-1,-1):
        adjust_heap(A,heap_size,i)
        
def adjust_heap(A,heap_size,i):
    left = 2*i +1
    right = 2*i+2
    largest = left if left < heap_size and A[left] > A[i] else i
    largest = right if right < heap_size and A[right] >A[largest] else largest
    if i != largest:
        A[i],A[largest] = A[largest],A[i]
        adjust_heap(A,heap_size,largest)
        
A = [9,1,2,4,5,8,9,4,4]
print(heap_sort(A))

