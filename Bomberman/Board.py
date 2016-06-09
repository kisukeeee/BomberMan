# coding=utf-8
class Board:
    def __init__(self, width, height):
        # 初期化：空のリストがマップの要素
        self.board = [[[] for col in range(width)] for row in range(height)]
        # ガベも作る.Objectで.

    def getBoject(self, x, y):
        """Board上にあるものを返す."""

    def putObject(self, Object):
        """ボムなりオブジェクトなりをBoardへ追加."""

    def deleteObject(self, x, y, Class):
        """
        Board上からオブジェクトを削除.
        Classにはclassを指定.
        """
    def display(self):
        for i in range(1,W-1):
            for j in range(1,H-1):
                # class がなにかしらべてclassごとに表示する.
                print("disp")
