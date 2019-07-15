# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:04:42 2019

@author: Administrator
"""

'''
QS: 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

思路： 递归思想 将复杂问题简单化 比如二叉树为 [2,4,7] 就只有一个节点 一个左孩子 一个右孩子 
                                扩展开为 一个节点 一个左子树 一个右子树
      前序遍历：根结点 ---> 左子树 ---> 右子树
      中序遍历：左子树---> 根结点 ---> 右子树
      后序遍历：左子树 ---> 右子树 ---> 根结点
      层次遍历：只需按层次遍历即可

第一次：     
前序： [1, 2, 4, 7, 3, 5, 6, 8] 节点1 左子树：[2, 4, 7] 右子树：[3, 5, 6, 8]
中序： [4, 7, 2, 1, 5, 3, 8, 6] 节点1 左子树: [4, 7, 2] 右子树：[5, 3, 8, 6]

第二次：
前序: [2, 4, 7] 节点：2 左子树：[4] 右子树：[7]
中序：[4, 7, 2] 节点：2 左子树：[4] 右子树：[7]

...

'''
class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right
    
def construct_tree(pre_order, mid_order):
  if len(pre_order) == 0 or len(mid_order) ==0 :
    return None
  # 前序遍历的第一个结点一定是根结点
  root_data = pre_order[0]
  for i in range(0, len(mid_order)):
    if mid_order[i] == root_data: #找到跟节点位置
      break 
  # 递归构造左子树和右子树
  # 中序遍历中节点左边的为左子树 可以查出左子树的长度i；
  # 前序遍历第一个为节点后面为左节点和右节点 根据上面的i 可以确定前序的左子树的长度
  left = construct_tree(pre_order[1 : 1 + i], mid_order[:i])
  right = construct_tree(pre_order[1 + i:], mid_order[i+1:])
  return Node(root_data, left, right)

if __name__ == '__main__':
  pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
  mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
  root = construct_tree(pre_order, mid_order)
  print (root.data)

