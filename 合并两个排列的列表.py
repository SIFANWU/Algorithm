# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:59:31 2019

@author: Administrator
"""
'''
QS:输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则

思路：phead1: 1 3 5
     phead2: 2 4 6
     第一个位置比较 小的存到结果 并且删去 直到 一个序列没有元素停止
    
'''

def Merge(pHead1, pHead2):
    result = []
    while True:
        if len(pHead1)==0 :
            result.extend(pHead2)
            print (result)
            return 
        if len(pHead2)==0 :
            result.extend(pHead1)
            print (result)
            return 
        if pHead1[0] >= pHead2[0]:
            result.append(pHead2[0])
            pHead2.pop(0)
        else:
            result.append(pHead1[0])
            pHead1.pop(0)
      
a =[1,3,5]
b =[2,4,6]       
Merge(a,b)
            
    