#coding:UTF-8"

from Bom import Bom
from Player import Player
from Object import Object
from Board import Board

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
