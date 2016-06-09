#coding:UTF-8"
import sys
import math
import string
import numpy as np
from Bom import Bom
from Board import Board

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
