maze = [[]]
dirs = [
    lambda x, y:(x+1, y),
    lambda x, y:(x-1, y),
    lambda x, y:(x, y+1),
    lambda x, y:(x, y-1),
]


def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while(len(stack)>0):
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            #走到终点了
            for p in stack:
                print(p)
            return True
        # x, y 四个方向 x-1 y
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2
                break
        else:
            # 回退
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路")
        return False