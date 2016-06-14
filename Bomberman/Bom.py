# coding=utf-8
class Bom:
    def __init__(self, x, y, fire, time):
        self.x = x
        self.y = y
        self.fire = fire    # 火力
        self.time = time    # 爆発するまでのターン数
        self.up = self.down = self.right = self.left = self.fire
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
            self.bom_var(i,Object)
            self.bom_side(i,Object)
        while(True):
            count = 0
            for i in Bom:
                if i.flag == 1:
                    self.bom_chain(i,Bom)

            for i in Bom:
                if i.flag == 1 and i.time != 1:
                    self.bom_side(i,Object)
                    self.bom_var(i,Object)
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

    def bom_var(self,Bom,Object):
        if Bom.flag == 1:
            # Bom.up = Bom.down = Bom.fire # 生成時に初期化したのでコメントアウト
            for i in Object:
                if Bom.x == i.x:
                    if Bom.y - Bom.up <= i.y and Bom.y > i.y:
                        Bom.up = Bom.y - 1 - i.y
                        print("#up"+str(i.y)+","+str(i.x)+","+str(Bom.up))
                        if Bom.up < 0:
                            Bom.up = 0
                    if Bom.y + Bom.down >= i.y and Bom.y < i.y:
                        Bom.down = i.y - Bom.y - 1
                        print("#dw"+str(i.y)+","+str(i.x)+","+str(Bom.down))
                        if Bom.down < 0:
                            Bom.down = 0


    def bom_side(self,Bom,Object):
        if Bom.flag == 1:
            # Bom.right = Bom.left = Bom.fire # 生成時に初期化したのでコメントアウト
            for i in Object:
                if Bom.y == i.y:
                    if Bom.x - Bom.left <= i.x and Bom.x > i.x:
                        Bom.left = Bom.x - 1 - i.x
                        print("#le"+str(i.y)+","+str(i.x)+","+str(Bom.left))
                        if Bom.left < 0:
                            Bom.left = 0
                    if Bom.x + Bom.right >= i.x and Bom.x < i.x:
                        Bom.right = i.x - Bom.x - 1
                        print("#ri"+str(i.y)+","+str(i.x)+","+str(Bom.right))
                        if Bom.right < 0:
                            Bom.right = 0

    def bom_chain(self,burn_Bom,Bom):
        for i in Bom:
            if burn_Bom.x == i.x and burn_Bom.y == i.y:
                continue
            if i.flag == 1:
                continue

            if burn_Bom.y == i.y:
                if burn_Bom.x + burn_Bom.right >= i.x and burn_Bom.x - burn_Bom.left  <= i.x:
                    i.flag = 1

            if burn_Bom.x == i.x:
                if burn_Bom.y - burn_Bom.up <= i.y and burn_Bom.y + burn_Bom.down >= i.y:
                    i.flag = 1

    def decision(self,Human,Bom):
        for i in Human:
            for bom in Bom:
                if bom.x == i.x:
                    if bom.flag == 1 and bom.y + bom.down >= i.y and bom.y - bom.up <= i.y:
                        i.did = True

                if bom.y == i.y:
                    if bom.flag == 1 and bom.x + bom.right >= i.x and bom.x - bom.left <= i.x:
                        i.did = True
