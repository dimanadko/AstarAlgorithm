import math

h = 8
w = 8

red = [[0 for x in range(w)] for y in range(h)]
green = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def pointOfRoot(self, numb):
        self.numb = numb
    def left(self, finish):
        self.way = math.fabs(self.x-finish.x) + math.fabs(self.y-finish.y)
        return self.way
    def isGreen(self, red):
        if(red[self.y][self.x] == 0 and self.y*self.x>=0 and self.y<9 and self.x<9):
            return True



def findWayOut( maze , start, finish, curNumb, red, green):

    print("Current point is: "  + str(start.x) + " " + str(start.y) )
    red[start.y][start.x] = 1
    top = Point(start.x, start.y-1)
    bot = Point(start.x, start.y+1)
    right = Point(start.x+1, start.y)
    left = Point(start.x-1, start.y)
    temp = [top, right, bot, left]
    temp = list(filter(lambda x: x.isGreen(red), temp))
    green.extend(temp)
    green = sorted(green, key=lambda x: x.left(finish))
    for i in range(len(green)):
        print (green[i].x, green[i].y)
    print("----")
    if (len(temp)):
        maze[start.y][start.x] = str(curNumb)
        curNumb+=1

    if (start.x == finish.x and start.y== finish.y):
        maze[start.y][start.x] = str(curNumb)
        return True
    findWayOut ( maze , green.pop(0), finish, curNumb, red, green)




maze = [
        ['x','x','x','x','x','x','x','x'],
        ['x',' ',' ',' ',' ','x',' ','x'],
        ['x',' ','x',' ','x','x',' ','x'],
        ['x',' ','x',' ',' ',' ',' ','x'],
        ['x',' ','x',' ','x',' ','x','x'],
        ['x',' ','x',' ','x',' ','x','x'],
        ['x',' ','x',' ',' ',' ','x','x'],
        ['x','x','x','x','x','x','x','x']
    ]

for i in range(len(maze)) :
    for j in range(len(maze[i])):
        if (maze[i][j] == 'x'):
            red[i][j] = 1
print (red)

start = Point(1, 5)
finish = Point(6, 1)

findWayOut( maze, start, finish, 1, red, green)

for arr in maze:
    print(arr)
