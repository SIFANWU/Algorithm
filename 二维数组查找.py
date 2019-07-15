# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:13:13 2019

@author: Administrator
"""
'''
QS；在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

思路： 观察到左下角的元素 比它大 向右找 比它小向上找 

'''

def Find(target, array):
    row = len(array)
    col = len(array[0])
    i = row-1
    j = 0
    while i>=0 and j<=(col-1):
        base = array[i][j]
        if base > target:
            i -=1
        elif base < target:
            j +=1 
        else:
            return print ('Y')
    return print ('N')
    
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]  
Find(7,array)    
    