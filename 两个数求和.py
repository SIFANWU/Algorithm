# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:08:51 2019

@author: Administrator
"""
'''
QS:给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

给定 nums = [2, 7, 11, 15], target = 9

返回 [0, 1]

思路：hash表格

'''


nums = [2, 7, 11, 15]
target = 9

mydict = {}
for i,j in enumerate(nums):
    mydict[j] = i
    
for i,j in enumerate(nums):
    k = mydict.get(target-j)
    if k is not None:
        print ([i,k])
    


