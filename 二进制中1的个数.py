# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:18:45 2019

@author: Administrator
"""

'''
QS:输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

思路：    
整数12的二进制表示为1100，将其减一变为1011，将得到的结果和原树进行按位与，得到1000，
所以发现规律没有？把一个整数减去1之后再和原来的整数做按位与，
得到的结果相当于是把整数的二进制表示中最右边的一个1变成0，按照这个规律进行遍历，
则函数的循环次数为二进制中一的个数次
'''
def num_of_one(num):
    '''
    count the num of "one" in num n
    bin():convert the num to binary string
    :param num: num num
    :return: the num of "one" in num
    '''
    if num >= 0:
        nbin = bin(num)
        return nbin.count('1')
    else:
        num = abs(num)
        nbin = bin(num-1)
        return 32 - nbin.count('1')\
    
print (num_of_one(-10))