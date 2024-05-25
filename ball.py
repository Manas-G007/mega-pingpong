import pygame as pyg
class Ball:
    def __init__(self,path,x,y,speed):
        self.ball=pyg.image.load(path)
        self.x=x
        self.y=y
        self.speedX=speed
        self.speedY=speed
    
    def setPos(self,x,y):
        self.x=x
        self.y=y
    
    def dirX(self):
        self.speedX=-self.speedX
    
    def dirY(self):
        self.speedY=-self.speedY
    