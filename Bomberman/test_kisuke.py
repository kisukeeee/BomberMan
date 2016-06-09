#coding:UTF-8"
import sys
import math
import string
import numpy as np
from Bom import Bom

class Player:
    def __init__(self, x, y, fire, ID):
        self.x = x
        self.y = y
        self.fire = fire
        self.ID = ID
        self.did = False

    def move(self, direction, mv_rg):
        if 'up' in direction and mv_rg[0] > 0:
            self.y -= 1
        elif 'dw' in direction and mv_rg[1] > 0:
            self.y += 1
        elif 'ri' in direction and mv_rg[2] > 0:
            self.x += 1
        elif 'le' in direction and mv_rg[3] > 0:
            self.x -= 1

    def createBom(self):
        bom = Bom(x=self.x, y=self.y, fire=self.fire, time=3)
        return bom

class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.hardness = hardness

'''
class Bom:
    def __init__(self, x, y, fire):
        self.x = x
        self.y = y
        self.fire = fire
        self.time = 1
        self.up = 2
        self.down = 2
        self.right = 2
        self.left = 2
'''

class Board:
    def __init__(self, width, height):
        # 初期化：空のリストがマップの要素
        
        self.board = [[[] for col in range(width + 2)] for row in range(height + 2)]
        for i in range(width + 2):
            self.board[0][i].append(Object(x=i,y=0))
            self.board[width + 1][i].append(Object(x=i, y=width+1))
        for i in range(1,height + 1):
            self.board[i][0].append(Object(x=0, y=i))
            self.board[i][height + 1].append(Object(x=height+1, y=i))
        #self.board[height + 1][width + 1].append(Object(x=height+1,y=width+1))
        
        self.width = width
        self.height = height
        # boardの大きさに合ったObject生成
        for i in range(2, self.height, 2):
            for j in range(2, self.width, 2):
                self.putObject(Object(x=j, y=i))
            
        """
        self.board[2][2].append(Object(x=2,y=2))
        self.board[2][4].append(Object(x=2,y=4))
        self.board[4][2].append(Object(x=4,y=2))
        self.board[4][4].append(Object(x=4,y=4))
        """
    def class_check(self, cla: list):
        for i in cla:
            if isinstance(i, Object) or isinstance(i, Bom):
                return False
        return True

    def movable_range(self,player: Player):
        # 返り値はリストで[up,dw,ri,le]それぞれの移動できる距離を格納
        range = [0, 0, 0, 0]
        flag = [1, 1, 1, 1]
        flag2 = 0
        direc = 1
        while True:
            # up
            if (player.y - direc) > 0 and flag[0] is 1:
                if self.class_check(self.board[player.x][player.y - direc]):
                    range[0] += 1
                else:
                    flag[0] = 0
            # dw
            if(player.y + direc) < len(self.board) and flag[1] is 1:
                if self.class_check(self.board[player.x][player.y + direc]):
                    range[1] += 1
                else:
                    flag[1] = 0
            # ri
            if (player.x + direc) < len(self.board) and flag[2] is 1:
                if self.class_check(self.board[player.x + direc][player.y]):
                    range[2] += 1
                else:
                    flag[2] = 0
            # le
            if (player.x - direc) > 0 and flag[3] is 1:
                if self.class_check(self.board[player.x - direc][player.y]):
                    range[3] += 1
                else:
                    flag[3] = 0
            direc += 1
            if flag2 == sum(range):
                break
            flag2 = sum(range)
        #print(range)
        return range

    def getObject(self, x, y):
        """Board上にあるものを返す."""

    def putObject(self, object):
        """ボムなりオブジェクトなりをBoardへ追加."""
        self.board[object.y][object.x].append(object)

    def deleteObject(self, x, y, cla):
        """
        Board上からオブジェクトを削除.
        Classにはclassを指定.
        """
    
    def getClassList(self, Class):
        ret = []
        for x in range(self.width):
            for y in range(self.height):
                for obj in self.board[y][x]:
                    if (isinstance(obj, Class)):
                        ret.append(obj)
        return ret

    def display(self, p: Player):
        BurstBoard = np.zeros((self.height+2, self.width+2)).astype(np.int32)
        Boms = self.getClassList(Bom)
        for bom in Boms:
            if bom.flag == 1:
                BurstBoard[bom.x-bom.left:bom.x+bom.right+1, bom.y] = 1
                BurstBoard[bom.x, bom.y-bom.up:bom.y+bom.down+1] = 1

        
        for x in range(self.width + 2):
            for y in range(self.height + 2):
                if BurstBoard[y, x] == 1:
                    sys.stdout.write('*')
                elif p.x == y and p.y == x:
                    sys.stdout.write(p.ID)
                elif self.board[x][y] != []:
                        for obj in self.board[x][y]:
                            if(isinstance(obj,Bom)):
                                sys.stdout.write("o")
                            elif(isinstance(obj,Object)):
                                sys.stdout.write("@")
                else:
                    sys.stdout.write(' ')
            print()


def main():
    board = Board(width=5, height=5)
    print(board.board)
    board.display()
    player = []
    for i in range(4):
        print(chr(65+i))
        print('input start x')
        startx = int(input().strip())
        print('input start y')
        starty = int(input().strip())
        player.append(Player(x=startx, y=starty, fire=2, ID=chr(65+i)))
        print(board.display())
    while True:
        print('input direction')
        directions = input().strip().split()
        for i in range(len(player)):
            player[i].move(directions, board.movable_range(player[i]))
        print(board.display())

p = []
if __name__ == '__main__':
    # main()
    board = Board(width=9, height=9)
    player = Player(x=3, y=3, fire=2, ID=chr(65))
    p.append(player)
    board.display(player)
    while True:
        print('input direction')
        directions = input().strip()
        if '1' in directions:
            board.putObject(player.createBom())
        elif 'q' in directions:
            break
        player.move(directions, board.movable_range(player))
        #print(board.getClassList(Bom))
        Bom(1,1,1,1).calcBurstArea(board.getClassList(Bom), board.getClassList(Object), board, p)
        board.display(player)