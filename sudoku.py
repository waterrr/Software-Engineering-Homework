#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   sudoku.py
@Contact :   admin@gksec.com
@License :   (C)Copyright 2007, GNU General Public License V3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/26 15:28   W4ter      1.0         None
"""

class point:
"""
初始化方法
建立坐标系
"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0


def rowNum(p,sudoku):
"""
判断行
:return:
"""
    row = set(sudoku[p.y * 4:(p.y + 1) * 4])
    row.remove(0)
    return row


def colNum(p,sudoku):
"""
判断列
:return:
"""
    col = []
    length = len(sudoku)
    for i in range(p.x,length,4):
        col.append(sudoku[i])
    col = set(col)
    col.remove(0)
    return col


def initPoint(sudoku):
"""
找到需要填充的位置
:return:
"""
    pointList = []
    length = len(sudoku)
    for i in range(length):
        if sudoku[i] == 0:
            p = point(i % 4,i // 4)   #遍历所有的点
            for j in range(1,5):      #找到不重复的结果
                if j not in rowNum(p,sudoku) and j not in colNum(p,sudoku):
                    p.available.append(j)
            pointList.append(p)
    return pointList


def tryInsert(p,sudoku):
"""
对于每个需要的位置进行填充
:return:
"""
    availNum = p.available
    for v in availNum:
        p.value = v
        if check(p,sudoku):
            sudoku[p.y*4 + p.x] = p.value
            if len(pointList) <= 0:
                exit()
            p2 = pointList.pop()
            tryInsert(p2,sudoku)
            sudoku[p2.y * 4 + p2.x] = 0
            sudoku[p.y * 4 + p.x] = 0
            p2.value = 0
            pointList.append(p2)
        else:
            pass


def check(p,sudoku):
"""
判断填充条件
:return:
""" 
    #如果为0就不填充
    if p.value == 0:
        return False
    #再次检查填充的点是否与当前已经填充的点重复
    if p.value not in rowNum(p,sudoku) and p.value not in colNum(p,sudoku):
        return True
    else:
        return False
        

if __name__ == '__main__':
    sudoku = [
        4,0,0,0,
        0,0,0,1,
        0,0,1,0,
        0,0,3,4,
    ]
    pointList = initPoint(sudoku)
    p = pointList.pop()
    tryInsert(p,sudoku)
