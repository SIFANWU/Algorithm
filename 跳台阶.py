# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:57:08 2019

@author: Administrator
"""

'''
Qs:一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

思路 ：递归 从后往前想
    第n个台阶 只能由 n-1 或者 n-2 可以跳到
    f[n] = f[n-1]+f[n-2] 斐波那契数列
    ...
    同理递推：
    前提：f[1]=1 f[2]=2
    f[3] =f[2] +f[1]

'''

def jumpFloor(self, n):
    mylist = [1,1,2]
    while len(mylist)<=n:
        mylist.append(mylist[-1]+mylist[-2])
    return mylist[n]