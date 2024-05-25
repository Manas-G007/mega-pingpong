import pygame as pyg

class Slabe:
    def __init__(self,path,x,y,speed):
        self.slabe=pyg.image.load(path)
        self.x=x
        self.y=y
        self.speed=speed

    def setPos(self,x,y):
        self.x=x
        self.y=y

    def direction(self,speed):
        self.speed=speed