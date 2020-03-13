#!/user/bin/env.python
# _*_ coding:utf-8 _*_
# @author:W4ter

from collections import deque

MAX_VALUE = 0x7fffffff


# 创建坐标
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# 宽度优先搜索算法实现
def bfs(maze, begin, end):
    n, m = len(maze), len(maze[0])
    dist = [[MAX_VALUE for _ in range(m)] for _ in range(n)]
    pre = [[None for _ in range(m)] for _ in range(n)]  # 当前点的上一个点,用于输出路径轨迹

    dx = [1, 0, -1, 0]  # 四个方位
    dy = [0, 1, 0, -1]
    sx, sy = begin.x, begin.y
    gx, gy = end.x, end.y

    dist[sx][sy] = 0
    queue = deque()
    queue.append(begin)
    while queue:
        curr = queue.popleft()
        find = False
        for i in range(4):
            nx, ny = curr.x + dx[i], curr.y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '1' and dist[nx][ny] == MAX_VALUE:
                dist[nx][ny] = dist[curr.x][curr.y] + 1
                pre[nx][ny] = curr
                queue.append(Point(nx, ny))
                if nx == gx and ny == gy:
                    find = True
                    break
        if find:
            break
    if int(dist[gx][gy]) < 1000:
        print(dist[gx][gy])
    else:
        print("No solution")


if __name__ == '__main__':
    n = int(input())
    maze = [[0] * n] * n
    for i in range(n):
        maze[i] = input().split(' ')
    begin = Point()
    end = Point()
    begin.x = 1
    begin.y = 1
    end.x = (n-2)
    end.y = (n-2)
    bfs(maze, begin, end)
