# coding=utf-8
class Bom:
    def __init__(self, x, y, fire, time):
        self.x = x
        self.y = y
        self.fire = fire    # 火力
        self.time = time    # 爆発するまでのターン数
        self.up = 0
        self.down = 0
        self.right = 0
        self.left = 0
        self.flag = 0

    def isBurst(self):
        if self.time == 1:
            return True
        else:
            return False

    def calcBurstArea(self,Bom,Object,Board,Human:list):
        for i in Bom:
           # print(i.right)
           # print(i.left)
           # print(i.up)
           # print(i.down)
            self.bom_time(i)
            self.bom_var(i,Object,Board.height)
            self.bom_side(i,Object,Board.width)
        while(True):
            count = 0
            for i in Bom:
                if i.flag == 1:
                    self.bom_chain(i,Bom)

            for i in Bom:
                if i.flag == 1 and i.time != 1:
                    self.bom_side(i,Object,Board.width)
                    self.bom_var(i,Object,Board.height)
                    i.time = 1
                    count = count + 1

            if count == 0:
                break
        #Bom = sorted(Bom,lambda = x :x.time)
        for i in Bom:
            if i.flag == 0:
                break
            #self.decision(i,Human)
        '''
        for i in Bom:
            if i.flag == 1:

        '''
        """
        爆発の範囲を計算して返す.
        どうゆう形で返すのがいいか.
        """

    def motionOfHitObject(self):
        """
        各物体に当たった時の処理を書く
        プレイヤー：die を Trueに
        オブジェクト：hardnessを減らす・壊す.
        """
    def bom_time(self, Bom):
        if Bom.time > 1:
            Bom.time = Bom.time - 1
        elif Bom.time == 1:
            Bom.flag = 1

    def bom_var(self,Bom,Object,H):
        if Bom.flag == 1:
            for i in range(1,Bom.fire+1):
                if Bom.y+i > H:
                    Bom.down  = Bom.down + 1
                elif Bom.y-i <= 0:
                    Bom.up = Bom.up + 1
                else:
                    Bom.down = Bom.down + 1
                    Bom.up = Bom.up + 1

            for i in Object:
                if Bom.x == i.x:
                    if Bom.y + Bom.up > i.y:
                        Bom.up = Bom.up - i.y
                        if Bom.up < 0:
                            Bom.up = 0
                    if Bom.y - Bom.left < i.y:
                        Bom.down = i.y - (Bom.y - Bom.down)
                        if Bom.down < 0:
                            Bom.down = 0
                print(Bom.up)

    def bom_side(self,Bom,Object,W):
        if Bom.flag == 1:
            for i in range(1,Bom.fire+1):
                if Bom.x+i > W:
                    Bom.left  = Bom.left + 1
                elif Bom.x-i <= 0:
                    Bom.right = Bom.right + 1
                else:
                    Bom.left = Bom.left + 1
                    Bom.right = Bom.right + 1

            for i in Object:
                if Bom.y == i.y:
                    if Bom.x < i.x:
                        if Bom.x + Bom.right > i.x:
                            Bom.right = Bom.x + Bom.right - i.x
                            if Bom.right < 0:
                                Bom.right = 0
                    else:
                        if Bom.x - Bom.left < i.x:
                            Bom.left  = i.x - (Bom.x - Bom.left)
                            if Bom.left < 0:
                                Bom.left = 0

    def bom_chain(self,burn_Bom,Bom):
        for i in Bom:
            if burn_Bom.x == i.x and burn_Bom.y == i.y:
                continue
            if i.flag == 1:
                continue

            if burn_Bom.y == i.y:
                if burn_Bom.x + burn_Bom.right > i.x:
                    i.flag = 1
                if burn_Bom.x - burn_Bom.left  < i.x:
                    i.flag = 1

            if burn_Bom.x == i.x:
                if burn_Bom.y + burn_Bom.up > i.y:
                    i.flag = 1
                if burn_Bom.y - burn_Bom.down < i.y:
                    i.flag = 1

    def decision(self,Human,Bom):
        for i in Human:
            if Bom.x == i.x:
                if Bom.y + Bom.up >= i.y or Bom.y - Bom.down <= i.y:
                    i.die = True

            if Bom.y == i.y:
                if Bom.x + Bom.right >= i.x or Bom.x - Bom.left <= i.x:
                    i.die = True
