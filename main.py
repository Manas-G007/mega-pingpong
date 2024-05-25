import pygame as pyg
import numpy as np
from time import sleep
from ball import Ball
from slabe import Slabe
from text import Text

pyg.init()

disp=pyg.display

# styling
bgLight=30,30,30
white=255,255,255

# disp config
running=True
stop=False
screenSize=800,600
size=50
slabeSpeed=0.4
counter=10
score=[0,0]
icon=pyg.image.load("assets/icon.png")
disp.set_icon(icon)
screen=disp.set_mode(screenSize)
disp.set_caption("Ping Pong")

# elements
sign=[-0.4,0.4]
b1=Ball("assets/ball.png",
            screenSize[0]/2 - size/2,
            screenSize[1]/2 - size/2
            ,sign[np.random.randint(0,1)])
s1=Slabe("assets/slabe1.png",0,0,0)
s2=Slabe("assets/slabe2.png",screenSize[0]-size/2,0,0)

def resetGame():
    global score , stop, counter
    s1.setPos(0,0)
    s2.setPos(screenSize[0]-size/2,0)
    score[0],score[1]=0,0
    stop=False
    counter=10

def checkWin():
    global stop
    if score[0]==3:
        stop=True
    elif score[1]==3:
        stop=True

def resetBall():
    global score
    if b1.x<0 :
        b1.setPos(screenSize[0]/2 - size/2,
            screenSize[1]/2 - size/2)
        
        b1.dirX()
        b1.dirY()
        score[1]+=1
    if b1.x>screenSize[0]:
        b1.setPos(screenSize[0]/2 - size/2,
            screenSize[1]/2 - size/2)
        
        b1.dirX()
        b1.dirY()
        score[0]+=1

def hitSlabe1():
    if b1.x<size/2 and b1.y>s1.y and b1.y<s1.y + size*2 :
        b1.dirX()

def hitSlabe2():
    if b1.x>screenSize[0]-1.5*size and b1.y>s2.y and b1.y<s2.y + size*2 :
        b1.dirX()

def restrictSlabe1():
    if s1.y<0 or s1.y>screenSize[1] - size*2:
        s1.direction(0)

def restrictSlabe2():
    if s2.y<0 or s2.y>screenSize[1] - size*2:
        s2.direction(0)

def moveSlabe1(key):
    if key==pyg.K_w:
        s1.direction(-0.5)
    elif key==pyg.K_s:
        s1.direction(0.5)

def moveSlabe2(key):
    if key==pyg.K_UP:
        s2.direction(-0.5)
    elif key==pyg.K_DOWN:
        s2.direction(0.5)

def boundary():
    if b1.y<0 or b1.y>screenSize[1] - size:
        b1.dirY()

def showWinner():
    screen.blit(Text("Player 1 Win" if score[0]==3 else "Player 2 Win",white)
                .text,(screenSize[0]/2 - 2.4*size ,screenSize[1]/2 - size/2))
    
def renderScore():
    screen.blit(Text(f"{score[0]}:{score[1]}",white).text,(screenSize[0]/2 - 0.9*size , 10))

def renderSlabe1():
    screen.blit(s1.slabe,(s1.x,s1.y))

def renderSlabe2():
    screen.blit(s2.slabe,(s2.x,s2.y))

def renderBall():
    screen.blit(b1.ball,(b1.x,b1.y))

def update():
    global running,counter
    while running:
        for event in pyg.event.get():
            if event.type==pyg.QUIT:
                running=False
            if event.type==pyg.KEYDOWN:
                # w and s
                moveSlabe1(event.key)
                # up and down arrow
                moveSlabe2(event.key)

            if event.type==pyg.KEYUP:
                s1.direction(0)
                s2.direction(0)

        if stop:
            screen.fill(bgLight)
            showWinner()
            if counter==0:
                resetGame()
            else:
                screen.blit(Text(f"Game restarts in {counter}!!",white)
                .text,(screenSize[0]/2 - 3.3*size ,screenSize[1]/1.8))
                sleep(1)
                counter-=1
        else:
            # movement
            b1.setPos(b1.x+b1.speedX,
                    b1.y+b1.speedY)
            
            s1.setPos(s1.x,s1.y+s1.speed)
            s2.setPos(s2.x,s2.y+s2.speed)

            # boundary
            boundary()
            restrictSlabe1()
            restrictSlabe2()

            # hit
            hitSlabe1()
            hitSlabe2()

            # reset ball
            resetBall()

            # win check
            checkWin()

            # rendering
            screen.fill(bgLight)
            renderBall()
            renderSlabe1()
            renderSlabe2()
            renderScore()
        disp.update()

def main():
    update()

if __name__ == "__main__":
    main()