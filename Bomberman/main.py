#coding:UTF-8"

from Bom import Bom
from Player import Player
from Object import Object
from Board import Board

p = []
if __name__ == '__main__':

    board = Board(width=9, height=9)
    p.append(Player(x=5, y=5, fire=2, ID=chr(65)))
    p.append(Player(x=6, y=5, fire=2, ID=chr(66)))
    board.display(p)

    while True:
        print('input direction')
        directions = input().strip().split()
        for i, player in enumerate(p):  # ボム置く
            if '1' in directions[i]:
                board.putObject(player.createBom())
            elif 'q' in directions[i]:
                break
        for i, player in enumerate(p):  # 移動
            player.move(directions[i], board.movable_range(player))
        Bom(1,1,1,1).calcBurstArea(board.getClassList(Bom), board.getClassList(Object), board, p)
        Bom(1, 1, 1, 1).decision(p, board.getClassList(Bom))
        board.display(p)
        # 死亡処理
        for didPlayer in [x for x in p if x.did]:
            print(didPlayer.ID+" is died.")
        p=[x for x in p if not x.did]
        if len(p) == 1:
            print(p[0].ID + " おめ")
            break
        elif len(p) == 0:
            print("DRAW")
            break
    print("おつかれ")
