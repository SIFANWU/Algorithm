# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:26:11 2019

@author: Administrator
"""
'''
QS：打靶子问题 每一次得分0~10 一共打靶子n次 总得分m分 求所有可能组合
思路： 递归思想 从后往前思考
    第 n 次   打靶子得分 f[n] = remain - f[n-1]  
    第 n-1 次 打靶子得分 f[n-1] = remain - f[n-2]
    第 n-2 次 打靶子得分 f[n-2] = remain - f[n-3]
    ...
    第 1 次  打靶子得分 f[1] = m - i ( 0<=i<=10)
    
结束循环的条件：
    remain 剩余分数 < 0 或者 大于 剩余最大得分（全部都打满分10分）
    n 剩余次数小于等于0 所有组合都完成 打印出最后结果.

代码实现：
    提前给定固定列表 用于填充数据
'''

def shot(n, remain, mylist):
    if(remain < 0 or remain > (n+1)*10 ):
        return
    if(n <= 0):
        mylist[0] = remain;
        print (mylist)
        global counter 
        counter +=1
    else:
        for score in range(11):
            mylist[n] = score;
            shot(n - 1, remain - score, mylist)
                    
if __name__ == "__main__":
    number = 3 #次数
    total = 10 #总分
    init = [0 for i in range(number)]
    counter = 0
    shot(number-1, total, init)
    print ('总次数：',counter)  
