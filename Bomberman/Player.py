# coding=utf-8
from Bom import Bom

class Player:
    def __init__(self, x, y, fire, ID):
        self.x = x
        self.y = y
        self.fire = fire
        self.ID = ID
        self.did = False

    def move(self, direction, dirange):
        if not self.did:
            if 'up' in direction and dirange[0] > 0:
                self.y -= 1
            elif 'dw' in direction and dirange[1] > 0:
                self.y += 1
            elif 'ri' in direction and dirange[2] > 0:
                self.x += 1
            elif 'le' in direction and dirange[3] > 0:
                self.x -= 1

    def createBom(self):
        if not self.did:
            bom = Bom(x=self.x, y=self.y, fire=self.fire, time=3)
            return bom

