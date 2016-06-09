# coding=utf-8
class Player:
    def __init__(self, x, y, fire, ID):
        self.x = x
        self.y = y
        self.fire = fire    # 火力
        self.ID = ID

    def move(self, msg):
        """
        msg は移動方向”up,do,le,ri”.
        msg に従って1マス分Playerの位置を変える.
        移動できない場合は何もしない.
        """
    def putBom(self):
        """
        自分のいる位置にボムを置く.
        ボムのリストに追加.
        """
